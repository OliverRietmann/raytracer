from numpy import argmax, array, inf, sign

from myobject.object import Object

class Box(Object):
    def __init__(self, lower_bound, upper_bound, **kwargs):
        if not all(l < u for l, u in zip(lower_bound, upper_bound)):
            raise ValueError("lower_bound must be component-wise smaller than upper_bound")
        super().__init__(**kwargs)
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

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

    def get_normal(self, p):
        """
        Ersetzen Sie das 'return' statement unten durch
        Ihren Code: Sei p ein Punkt auf dem Quader.
        Geben Sie den nach aussen zeigenden, normierten
        Normalenvektor auf dem Quader am Punkt p zurück.
        Die beiden definierenden Ecken sind durch
        self.lower_bound und self.upper_bound abrufbar.
        """
        return array([0.0, 0.0, 0.0])
