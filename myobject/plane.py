from numpy import inf, inner

from myobject.object import Object, normalize

class Plane(Object):
    def __init__(self, n, d, **kwargs):
        super().__init__(**kwargs)
        self.n = n
        self.d = d

    def intersect(self, ray):
        v = ray.origin
        w = ray.direction

        """
        Ersetzen Sie diesen Kommentar durch Ihren Code:
        Gegeben ist ein Strahl mit Ursprung v und Richtung w.
        Geben Sie den Parameter t > 0 zurück, so dass v + t * w
        gerade der an v nächstgelegene Schnittpunkt des Strahls
        mit der Ebene ist. Falls dieser nicht existiert soll
        t = inf (also Unendlich) zurückgegeben werden. 
        """

        return inf

    def get_normal(self, p):
        return normalize(self.n)
