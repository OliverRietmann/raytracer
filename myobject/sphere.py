from numpy import array, inf, inner, sqrt

from myobject.object import Object, normalize


class Sphere(Object):
    def __init__(self, m, r, **kwargs):
        super().__init__(**kwargs)
        self.m = m
        self.r = r

    def intersect(self, ray):
        v = ray.origin
        w = ray.direction

        """
        Ersetzen Sie diesen Kommentar durch Ihren Code:
        Gegeben ist ein Strahl mit Ursprung v und Richtung w.
        Geben Sie den Parameter t > 0 zurück, so dass v + t * w
        gerade der an v nächstgelegene Schnittpunkt des Strahls
        mit der Kugel ist. Falls dieser nicht existiert soll
        t = inf (also Unendlich) zurückgegeben werden. 
        """

        return inf

    def get_normal(self, p):
        """
        Ersetzen Sie das 'return' statement unten durch
        Ihren Code: Sei p ein Punkt auf der Kugeloberfläche.
        Geben Sie den nach aussen zeigenden, normierten
        Normalenvektor auf der Kugel am Punkt p zurück.
        """
        return array([0.0, 0.0, 0.0])
