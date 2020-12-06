from numpy import array, inf, inner, pi
from numpy.linalg import norm

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

    def intersect(self, v, w):
        pass

    def get_normal(self, p):
        pass

    def _diffuse_shader(self, l, n):
        # Setzen Sie "diffuse_intensity" durch den
        # richtigen Wert gemäss diffuser Beleuchtung
        diffuse_intensity = 0.0
        return self.diffuse * diffuse_intensity * self.color

    def _specular_shader(self, c, l, n, light_color):
        m = self.phong[1]
        # Setzen Sie "specular_intensity" durch den
        # richtigen Wert gemäss diffuser Beleuchtung
        # Der exponent
        specular_intensity = 0.0
        return self.phong[0] * specular_intensity * light_color

    def _reflection_shader(self, c, n, p, lightsource_list, object_list, recursion_depth):
            # Ersetzen sie das "return" Statement
            # durch den korrekten Code
            return array([0.0, 0.0, 0.0])

    def shader(self, p, d, lightsource_list, object_list, recursion_depth=1):
        c = -normalize(d)       # Richtung aus der der Strahl gekommen ist
        n = self.get_normal(p)  # Normalenvektor am Punkt p

        # ambiente Beleuchtung
        color = self.ambient * self.color

        # Beleuchtungsmodell nach Phong
        if len(lightsource_list) > 0 and (self.diffuse > 0.0 or self.phong[0] > 0.0):
            # Für jede Lichtquelle berechne diffuse und spiegelnde Reflexion
            for lightsource in lightsource_list:
                # Licht-Strahl: v + t * w
                v = lightsource
                w = p - lightsource
                obj, t = get_nearest_obstacle(v, w, object_list)

                # Wenn die Lichtquelle nicht durch ein anderes Objekt verdeckt wird
                if t + 1.0e-10 > 1.0 and obj is self:
                    l = -normalize(w) # Richtung Lichtquelle
                    color += self._diffuse_shader(l, n)
                    color += self._specular_shader(c, l, n, array([1.0, 1.0, 1.0]))

        # perfekte Reflexion
        if self.reflection > 0.0 and Object.max_recursion_depth > recursion_depth:
            color += self._reflection_shader(c, n, p, lightsource_list, object_list, recursion_depth)

        return color
