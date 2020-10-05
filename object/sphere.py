from numpy import array, inf, inner, sqrt
from numpy.linalg import norm

from object.object import Object

def normalize(vector):
    return vector / norm(vector)

class Sphere(Object):
    def __init__(self, color, m, r):
        self.m = m
        self.r = r
        self.color = color

    def intersect(self, ray):
        v = ray.origin
        w = ray.direction
        
        a = inner(w, w)
        vm = v - self.m
        b = 2.0 * inner(vm, w)
        c = inner(vm, vm) - self.r**2
        
        d = b**2 - 4.0 * a * c
        
        if d >= 0.0:
            t0 = (-b - sqrt(d)) / (2.0 * a)
            t1 = (-b + sqrt(d)) / (2.0 * a)
            if t0 < 0.0 and t1 < 0.0:
                return inf
            elif t0 * t1 < 0.0:
                return max(t0, t1)
            else:
                return min(t0, t1)
        else:
            return inf

    def get_normal(self, p):
        return normalize(p - self.m)
