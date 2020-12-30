from numpy import array, inf, inner, pi
from numpy.linalg import norm

from core.tracer import get_nearest_obstacle

def normalize(vector):
    return vector / norm(vector)

class Object:
    max_recursion_depth = 5

    def __init__(self, color=array([1.0, 0.0, 0.0]), ambient=1.0, diffuse=0.0, reflection=0.0):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.reflection = reflection

    def intersect(self, v, w):
        pass

    def get_normal(self, p):
        pass

    @staticmethod
    def _diffuse_shader(self, l, n):
        """
        Ersetzen sie das "return" Statement durch den korrekten Code,
        so dass die Intensität gemäss diffuser Beleuchtung
        zurückgegeben wird.
        """
        return 0.0

    @staticmethod
    def _reflection_shader(self, c, n, p, lightsource_list, object_list, recursion_depth):
        """
        # Ersetzen sie das "return" Statement durch den korrekten Code,
        # so dass die Farbe am Schnittpunkt mit dem reflektierten Strahl
        # zurückgegeben wird. Trifft dieser kein Objekt, so soll schwarz
        # zurückgegeben werden.
        """
        return array([0.0, 0.0, 0.0])

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
