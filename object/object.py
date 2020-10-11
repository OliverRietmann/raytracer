from numpy import clip, inf, inner
from numpy.linalg import norm
from core.ray import Ray

def normalize(vector):
    return vector / norm(vector)

class Object:
    def __init__(self, properties):
        self.properties = properties

    def intersect(self, ray):
        pass

    def get_normal(self, p):
        pass

    def transform(self, matrix):
        pass

    def shader(self, p, lightsource, object_list):
        lightray = Ray(lightsource, p - lightsource)
        t = inf
        for obj in object_list:
            t = min(t, obj.intersect(lightray))
        #TODO: Find better solution that hardcoded epsilon 0.0001
        diffuse_coefficient = 0.0
        if t < inf and norm(p - lightray(t)) < 0.0001:
            normal = self.get_normal(p)
            light_direction = normalize(lightray.direction)
            diffuse_coefficient = inner(normal, -light_direction)
            diffuse_coefficient = clip(diffuse_coefficient, 0.0, 1.0)

        properties = self.properties
        return properties.color * (properties.ambient + properties.diffuse * diffuse_coefficient)
