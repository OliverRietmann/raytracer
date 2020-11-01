from numpy import array, clip, inner
from numpy.linalg import norm

from core.ray import Ray
from core.tracer import get_nearest_obstacle

def normalize(vector):
    return vector / norm(vector)

class Object:
    max_recursion_depth = 5
    counter = 0

    def __init__(self, properties):
        self.properties = properties
        self.id = Object.counter
        Object.counter += 1

    def intersect(self, ray):
        pass

    def get_normal(self, p):
        pass

    def transform(self, matrix):
        pass

    def shader(self, p, d, lightsource_list, object_list, recursion_depth=1):
        normal = self.get_normal(p)
        reflect = lambda incoming: incoming - 2.0 * inner(normal, incoming) * normal

        # ambient
        color = self.properties.ambient * self.properties.color

        # diffuse
        if self.properties.diffuse > 0.0:
            for lightsource in lightsource_list:
                lightray = Ray(lightsource, p - lightsource)
                nearest_obstacle, t = get_nearest_obstacle(lightray, object_list)
                if nearest_obstacle is not None and nearest_obstacle.id == self.id:
                    diffuse_coefficient = -inner(normal, normalize(lightray.direction))
                    diffuse_coefficient = clip(diffuse_coefficient, 0.0, 1.0)
                    color += self.properties.diffuse * diffuse_coefficient * self.properties.color

                    # Phong
                    if self.properties.phong[0] > 0.0 and self.properties.phong[1] > 0:
                        reflected = normalize(reflect(lightray.direction))
                        factor = -inner(reflected, normalize(d))
                        if factor > 0.0:
                            color += self.properties.phong[0] * factor**self.properties.phong[1] * array([1.0, 1.0, 1.0])

        # reflection
        if self.properties.reflection > 0.0 and Object.max_recursion_depth > recursion_depth:
            reflection_ray = Ray(p, d - 2.0 * inner(d, normal) * normal)
            obj, t = get_nearest_obstacle(reflection_ray, object_list)
            if obj is not None:
                reflection_color = obj.shader(reflection_ray(t), reflection_ray.direction, \
                lightsource_list, object_list, recursion_depth - 1)
                color += self.properties.reflection * reflection_color * self.properties.color

        return color
