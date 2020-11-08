from numpy import inf, inner

from object.object import Object, normalize

class Plane(Object):
    def __init__(self, n, d, **kwargs):
        super().__init__(**kwargs)
        self.n = n
        self.d = d

    #---intersect-begin---
    def intersect(self, ray):
        v = ray.origin
        w = ray.direction

        nw = inner(self.n, w)
        if nw < 0.0:
            t = -1.0 * (self.d + inner(self.n, v)) / nw
            if t > 0.0:
                return t

        return inf
    #---intersect-end---

    #---get_normal-begin---
    def get_normal(self, p):
        return normalize(self.n)
    #---get_normal-end---
