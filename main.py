from numpy import array, pi
from core.camera import Camera
from core.renderer import Renderer
from core.ray import Ray

from object.sphere import Sphere

camera = Camera(array([-1.0, 0.0, 1.0]), array([0.0, 0.0, 0.9]), 0.25 * pi, 640, 480)
renderer = Renderer(camera)
objects = []
objects.append(Sphere(array([1.0, 0.0, 0.0]), array([5.0, 0.0, 0.0]), 1.0))
objects.append(Sphere(array([0.0, 0.0, 1.0]), array([6.0, 2.0, 1.0]), 1.0))
lightsource = array([0.0, 0.0, 10.0])
renderer(lightsource, objects)
renderer.save_image("image.png")
