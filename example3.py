from numpy import array, pi

from core.camera import Camera
from core.renderer import Renderer
from myobject.sphere import Sphere
from myobject.plane import Plane

camera = Camera(array([-1.0, 0.0, 1.0]), array([0.0, 0.0, 1.0]), 0.25 * pi, 640, 480)
renderer = Renderer(camera)

lightsource = array([0.0, 0.0, 10.0])

sphere = Sphere(array([5.0, 0.0, 1.0]), 1.0, ambient=0.2, diffuse=0.8)

# Die Farbe Grün als RGB-Vektor
green = array([0.0, 1.0, 0.0])

# Wir zeichnen hier die xy-Ebene, also die Ebene mit
# Normalenvektor n = [0.0, 0.0, 1.0] und d = 0.0 in grün.
plane = Plane(array([0.0, 0.0, 1.0]), 0.0, color=green, ambient=0.2, diffuse=0.8)

renderer([lightsource], [sphere, plane], photo_exposure=0.0)
renderer.save_image("example3.png")
