#---plane-begin---
from numpy import inf, inner

from object.object import Object, normalize

class Plane(Object):
    def __init__(self, n, d, **kwargs):
        super().__init__(**kwargs)
        self.n = n # Normalenvektor n aus der Ebenengleichung
        self.d = d # Parameter d aus der Ebenengleichung

    def intersect(self, ray):
        # Der Strahl ist beschrieben durch v+t*w mit t>0
        v = ray.origin
        w = ray.direction

        # Falls der Strahl von "aussen" kommt, berechne s
        nw = inner(self.n, w)
        if nw < 0.0:
            s = -1.0 * (self.d + inner(self.n, v)) / nw
            if s > 0.0:
                return s

        # Falls kein zulässiger Schnittpunkt existiert,
        # wird "unendlich" zurückgegeben.
        return inf

    def get_normal(self, p):
        return normalize(self.n)
#---plane-end---
