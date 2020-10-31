from numpy import array, pi
from core.camera import Camera
from core.renderer import Renderer
from core.properties import Properties

from object.box import Box
from object.sphere import Sphere
from object.plane import Plane

camera = Camera(array([-10.0, 0.0, 2.0]), array([0.0, 0.0, 1.0]), 0.25 * pi, 640, 480)
renderer = Renderer(camera)

lightsource_list = [array([0.0, 5.0, 10.0]), array([-5.0, 10.0, 5.0])]

objects = []

red = array([1.0, 0.0, 0.0])
properties = Properties(red, 0.2, 0.8, 0.0)
objects.append(Sphere(array([4.0, -2.0, 0.0]), 1.0, properties))


purple = array([148.0 / 255.0, 0.0, 211.0 / 255.0])
properties = Properties(purple, 0.2, 0.2, 0.6)
objects.append(Sphere(array([6.0, 2.0, 1.0]), 2.0, properties))


blue = array([0.0, 0.0, 1.0])
properties = Properties(blue, 0.2, 0.8, 0.0)
objects.append(Box(array([-0.5, -3.0, -1.0]), array([0.5, -2.0, 0.0]), properties))


gray = array([0.7, 0.7, 0.7])
properties = Properties(gray, 0.2, 0.6, 0.2)
objects.append(Plane(array([0.0, 0.0, 1.0]), 1.0, properties))

renderer(lightsource_list, objects)
renderer.save_image("image.png")
