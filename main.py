from numpy import array, pi
from core.camera import Camera
from core.renderer import Renderer
from core.properties import Properties

from object.sphere import Sphere
from object.plane import Plane

camera = Camera(array([-1.0, 0.0, 1.0]), array([0.0, 0.0, 0.9]), 0.25 * pi, 640, 480)
renderer = Renderer(camera)

objects = []

lightsource_list = [array([0.0, 0.0, 10.0]), array([-5.0, 5.0, 10.0])]

red = array([1.0, 0.0, 0.0])
properties = Properties(red, 0.2, 0.8, 0.0)
objects.append(Sphere(array([5.0, -1.0, 0.0]), 1.0, properties))

blue = array([0.0, 0.0, 1.0])
properties = Properties(blue, 0.2, 0.2, 0.6)
objects.append(Sphere(array([6.0, 1.5, 0.75]), 1.0, properties))

gray = array([0.7, 0.7, 0.7])
properties = Properties(gray, 0.2, 0.6, 0.2)
objects.append(Plane(array([0.0, 0.0, 1.0]), 1.0, properties))

renderer(lightsource_list, objects)
renderer.save_image("image.png")
