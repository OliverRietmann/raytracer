from numpy import inf, inner, sqrt

from object.object import Object, normalize

class Sphere(Object):
    def __init__(self, m, r, **kwargs):
        super().__init__(**kwargs)
        self.m = m
        self.r = r

    #---intersect-begin---
    def intersect(self, ray):
        # Der Strahl ist beschrieben durch v+t*w mit t>0
        v = ray.origin
        w = ray.direction

        # Berechung der Koeffizienten der quadratischen Gleichung
        a = inner(w, w)
        mv = v - self.m
        b = 2.0 * inner(w, mv)
        c = inner(mv, mv) - self.r**2

        # Diskriminante
        d = b**2 - 4.0 * a * c

        # Fallunterscheidung: Schneidet der Strahl die Kugel?
        if d >= 0.0:
            t0 = (-b - sqrt(d)) / (2.0 * a)
            if t0 > 0.0 and inner(ray(t0) - self.m, w) < 0.0:
                return t0
            t1 = (-b + sqrt(d)) / (2.0 * a)
            if t1 > 0.0 and inner(ray(t1) - self.m, w) < 0.0:
                return t1

        # Falls kein Schnittpunkt existert, retourniere "unendlich"
        return inf
    #---intersect-end---

    #---get_normal-begin---
    def get_normal(self, p):
        return normalize(p - self.m)
    #---get_normal-end---
