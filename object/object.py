from numpy import array, inf, inner, pi
from numpy.linalg import norm

from core.tracer import get_nearest_obstacle

def normalize(vector):
    return vector / norm(vector)

class Object:
    def __init__(self, color=array([1.0, 0.0, 0.0]), ambient=1.0, diffuse=0.0, reflection=0.0):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.reflection = reflection

    def intersect(self, v, w):
        pass

    def get_normal(self, p):
        pass

    #---_diffuse_shader-begin---
    @staticmethod
    def _diffuse_shader(l, n):
        return max(0.0, inner(n, l))
    #---_diffuse_shader-end---

    #---_reflection_shader-begin---
    @staticmethod
    def _reflection_shader(c, n, p, lightsource_list, object_list, recursion_depth):
            # Gespiegelter Strahl p + t * c_prime, t > 0
            c_prime = 2.0 * inner(n, c) * n - c
            # Ermittle das getroffene Objekt obj und den Schnittpunkt-Parameter t
            obj, t = get_nearest_obstacle(p, c_prime, object_list)
            if t == inf:
                # Wenn kein Objekt getroffen wird: schwarz
                return array([0.0, 0.0, 0.0])
            else:
                # Berechne die Farbe am Punkt v + t * w
                return obj.shader(p + t * c_prime, -c_prime, lightsource_list, object_list, recursion_depth)
    #---_reflection_shader-end---

    #---shader-begin---
    def shader(self, p, c, lightsource_list, object_list, recursion_depth=5):
        c = normalize(c)       # Richtung aus der der Strahl gekommen ist
        n = self.get_normal(p) # Normalenvektor am Punkt p

        # ambiente Beleuchtung
        color = self.ambient * self.color

        # diffuse Beleuchtung
        if self.diffuse > 0.0 and len(lightsource_list) > 0:
            # Für jede Lichtquelle berechne diffuse und spiegelnde Reflexion
            for lightsource in lightsource_list:
                # Lichtstrahl: v + t * w
                v = lightsource
                w = p - lightsource
                obj, t = get_nearest_obstacle(v, w, object_list)
                # Wenn die Lichtquelle nicht durch ein anderes Objekt verdeckt wird
                if t + 1.0e-10 > 1.0 and obj is self:
                    l = -normalize(w) # Richtung Lichtquelle
                    color += self.diffuse * Object._diffuse_shader(l, n) * self.color

        # perfekte Reflexion
        if self.reflection > 0.0 and recursion_depth > 0:
            color += self.reflection * Object._reflection_shader(c, n, p, lightsource_list, object_list, recursion_depth - 1) * self.color

        return color
    #---shader-end---
