from numpy import array, inner, pi
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
        c = -normalize(d)       # Richtung aus der der Strahl gekommen ist
        n = self.get_normal(p)  # Normalenvektor am Punkt p

        # Funktion, die einen Vektor an der Normale n spiegelt
        reflect = lambda v: 2.0 * inner(n, v) * n - v

        # ambiente Beleuchtung
        color = self.ambient * self.color

        # Beleuchtungsmodell nach Phong
        if self.diffuse > 0.0 and len(lightsource_list) > 0:
            for lightsource in lightsource_list:
                shadowray = Ray(p, lightsource - p)
                l = normalize(shadowray.direction)
                nearest_obstacle, t = get_nearest_obstacle(shadowray, object_list)
                if t > 1.0:
                    # diffuse Reflexion
                    diffuse_intensity = max(0.0,  inner(n, l))
                    color += self.diffuse * diffuse_intensity * self.color

                    # spiegelnde Reflexion
                    if self.phong[0] > 0.0 and self.phong[1] > 0:
                        l_reflected = reflect(l)
                        factor = inner(l_reflected, c)
                        if factor > 0.0:
                            m = self.phong[1]
                            specular_intensity = (m + 2) / (2.0 * pi) * factor**m
                            color += self.phong[0] * specular_intensity * array([1.0, 1.0, 1.0])

        # Reflektion
        if self.reflection > 0.0 and Object.max_recursion_depth > recursion_depth:
            reflection_ray = Ray(p, reflect(c))
            obj, t = get_nearest_obstacle(reflection_ray, object_list)
            if obj is not None:
                reflection_color = obj.shader(reflection_ray(t), reflection_ray.direction, \
                lightsource_list, object_list, recursion_depth - 1)
                color += self.reflection * reflection_color * self.color

        return color
