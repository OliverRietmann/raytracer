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

    #---_diffuse_shader-begin---
    def _diffuse_shader(self, l, n):
        diffuse_intensity = max(0.0,  inner(n, l))
        return self.diffuse * diffuse_intensity * self.color
    #---_diffuse_shader-end---

    #---_specular_shader-begin---
    def _specular_shader(self, c, l, n):
        l_reflected = 2.0 * inner(n, l) * n - l
        factor = inner(l_reflected, c)
        specular_intensity = (self.phong[1] + 2) / (2.0 * pi) * factor**self.phong[1]
        return self.phong[0] * specular_intensity * array([1.0, 1.0, 1.0])
    #---_specular_shader-end---

    #---_reflection_shader-begin---
    def _reflection_shader(self, c, n, p, args):
            c_reflected = 2.0 * inner(n, c) * n - c
            reflection_ray = Ray(p, c_reflected)
            obj, t = get_nearest_obstacle(reflection_ray, args[1])
            if obj is None:
                return array([0.0, 0.0, 0.0])   # schwarz
            else:
                reflection_color = obj.shader(reflection_ray(t), reflection_ray.direction, *args)
                return self.reflection * reflection_color * self.color
    #---_reflection_shader-end---

    def shader(self, p, d, lightsource_list, object_list, recursion_depth=1):
        c = -normalize(d)       # Richtung aus der der Strahl gekommen ist
        n = self.get_normal(p)  # Normalenvektor am Punkt p

        # ambiente Beleuchtung
        color = self.ambient * self.color

        # Beleuchtungsmodell nach Phong
        if len(lightsource_list) > 0 and (self.diffuse > 0.0 or self.phong[0] > 0.0):
            # Für jede Lichtquelle berechne diffuse und spiegelnde Reflexion
            for lightsource in lightsource_list:
                lightray = Ray(lightsource, p - lightsource)
                l = -normalize(lightray.direction)
                nearest_obstacle, t = get_nearest_obstacle(lightray, object_list)

                # Wenn die Lichtquelle nicht durch ein anderes Objekt verdeckt wird
                if t + 1.0e-10 > 1.0 and nearest_obstacle is self:
                    # diffuse Reflexion
                    color += self._diffuse_shader(l, n)

                    # spiegelnde Reflexion
                    color += self._specular_shader(c, l, n)

        # perfekte Reflexion
        if self.reflection > 0.0 and Object.max_recursion_depth > recursion_depth:
            args = (lightsource_list, object_list, recursion_depth - 1)
            color += self._reflection_shader(c, n, p, args)

        return color
