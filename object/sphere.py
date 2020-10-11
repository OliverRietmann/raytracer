from numpy import inf, inner, sqrt

from object.object import Object, normalize

class Sphere(Object):
    def __init__(self, m, r, properties):
        super().__init__(properties)
        self.m = m
        self.r = r

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
