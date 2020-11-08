from numpy import array, clip, inner
from numpy.linalg import norm

from core.ray import Ray
from core.tracer import get_nearest_obstacle

def normalize(vector):
    return vector / norm(vector)

class Object:
    def __init__(self, color=array([1.0, 0.0, 0.0]), ambient=1.0, diffuse=0.0):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse

    def intersect(self, ray):
        pass

    def get_normal(self, p):
        pass

    def shader(self, p, d, lightsource_list, object_list):
        # Normalenvektor am betrachteten Punkt
        normal = self.get_normal(p)

        # Berechne ambiente (= globale) Beleuchtung
        color = self.ambient * self.color

        # Berechne diffuse Lichtreflexion
        if self.diffuse > 0.0 and len(lightsource_list) > 0:
            for lightsource in lightsource_list:
                # Strahl vom betrachteten Punkt zur Lichtquelle
                shadowray = Ray(p, lightsource - p)
                # Finde das erste Objekt, welches der Lichtstrahl schneidet
                nearest_obstacle, t = get_nearest_obstacle(shadowray, object_list)
                if t > 1.0 + 1.0e-15:
                    # Liegt kein Objekt zwischen p und der Lichtquelle, so berechne
                    # die diffuse Lichtreflexion am Punkt p
                    diffuse_coefficient = inner(normal, normalize(shadowray.direction))
                    diffuse_coefficient = clip(diffuse_coefficient, 0.0, 1.0)
                    color += self.diffuse * diffuse_coefficient * self.color

        return color
