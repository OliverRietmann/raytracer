from numpy import array, clip, inner
from numpy.linalg import norm

from core.ray import Ray
from core.tracer import get_nearest_obstacle

def normalize(vector):
    return vector / norm(vector)

class Object:
    max_recursion_depth = 5

    def __init__(self, color=array([1.0, 0.0, 0.0]), ambient=1.0, diffuse=0.0, phong=[0.0, 0], reflection=0.0):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.phong = phong
        self.reflection = reflection

    def intersect(self, ray):
        pass

    def get_normal(self, p):
        pass

    def shader(self, p, d, lightsource_list, object_list, recursion_depth=1):
        normal = self.get_normal(p)
        reflect = lambda incoming: incoming - 2.0 * inner(normal, incoming) * normal

        # ambient
        color = self.ambient * self.color

        # diffuse
        if self.diffuse > 0.0 and len(lightsource_list) > 0:
            for lightsource in lightsource_list:
                shadowray = Ray(p, lightsource - p)
                nearest_obstacle, t = get_nearest_obstacle(shadowray, object_list)
                if t > 1.0 + 1.0e-15:
                    diffuse_coefficient = inner(normal, normalize(shadowray.direction))
                    diffuse_coefficient = clip(diffuse_coefficient, 0.0, 1.0)
                    color += self.diffuse * diffuse_coefficient * self.color

                    # Phong
                    if self.phong[0] > 0.0 and self.phong[1] > 0:
                        reflected = normalize(reflect(shadowray.direction))
                        factor = inner(reflected, normalize(d))
                        if factor > 0.0:
                            color += self.phong[0] * factor**self.phong[1] * array([1.0, 1.0, 1.0])

        # reflection
        if self.reflection > 0.0 and Object.max_recursion_depth > recursion_depth:
            reflection_ray = Ray(p, reflect(d))
            obj, t = get_nearest_obstacle(reflection_ray, object_list)
            if obj is not None:
                reflection_color = obj.shader(reflection_ray(t), reflection_ray.direction, \
                lightsource_list, object_list, recursion_depth - 1)
                color += self.reflection * reflection_color * self.color

        return color
