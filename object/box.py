from numpy import argmax, array, inf, sign

from object.object import Object

class Box(Object):
    def __init__(self, lower_bound, upper_bound, **kwargs):
        if not all(l < u for l, u in zip(lower_bound, upper_bound)):
            raise ValueError("lower_bound must be component-wise smaller than upper_bound")
        super().__init__(**kwargs)
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    #---intersect-begin---
    def intersect(self, v, w):
        # Der Strahl ist beschrieben durch v+t*w mit t>0

        p = self.lower_bound
        q = self.upper_bound

        tp = array([-inf, -inf, -inf])
        tq = array([inf, inf, inf])

        for i in range(3):
            if w[i] == 0.0:
                if v[i] <= p[i] or q[i] <= v[i]:
                    return inf # Kein Schnittpunkt
            else:
                # Keine division durch Null
                tp[i] = (p[i] - v[i]) / w[i]
                tq[i] = (q[i] - v[i]) / w[i]

        # Schnittpunkt existiert wenn drei orthogonale Ebenen
        # hintereinander passiert werden.
        tmin = [min(sp, sq) for sp, sq in zip(tp, tq)]
        tmax = [max(sp, sq) for sp, sq in zip(tp, tq)]
        if max(tmin) <= min(tmax) and 0.0 < max(tmin):
            return max(tmin)

        return inf # Kein Schnittpunkt
    #---intersect-end---

    #---get_normal-begin---
    def get_normal(self, p):
        # Zentrum des Quaders
        c = 0.5 * (self.lower_bound + self.upper_bound)
        edges = self.upper_bound - self.lower_bound

        # Transformiere den Schnittpunkt in den Würfel [-0.5, 0.5]^3
        p_rel = (p - c) / edges

        # Welcher Seite liegt der Punkt am nächsten?
        i = argmax(abs(p_rel))
        n = array([0.0, 0.0, 0.0])
        n[i] = sign(p_rel[i])
        return n
    #---get_normal-end---
