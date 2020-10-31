from numpy import argmax, array, inf, sign

from object.object import Object, normalize
from object.plane import Plane

class Box(Object):
    def __init__(self, lower_bound, upper_bound, properties):
        if not all(l < u for l, u in zip(lower_bound, upper_bound)):
            raise ValueError("lower_bound must be component-wise smaller than upper_bound")
        super().__init__(properties)
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    #---intersect---
    def intersect(self, ray):
        v = ray.origin
        w = ray.direction

        t0 = (self.lower_bound - v) / w;
        t1 = (self.upper_bound - v) / w;

        tmin = [min(s0, s1) for s0, s1 in zip(t0, t1)]
        tmax = [max(s0, s1) for s0, s1 in zip(t0, t1)]

        if max(tmin) <= min(tmax) and 0.0 < max(tmin):
            return max(tmin)

        return inf
    #---end---

    #---normal---
    def get_normal(self, p):
        c = 0.5 * (self.lower_bound + self.upper_bound)
        edges = self.upper_bound - self.lower_bound
        p_rel = (p - c) / edges
        i = argmax(abs(p_rel))
        n = array([0.0, 0.0, 0.0])
        n[i] = sign(p_rel[i])
        return n
    #---normalend---
