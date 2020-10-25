#export PYTHONPATH="${PYTHONPATH}:/path/to/top/directory"

from numpy import array, pi
from core.camera import Camera
from core.renderer import Renderer
from core.properties import Properties

from object.sphere import Sphere

camera = Camera(array([-1.0, 0.0, 1.0]), array([0.0, 0.0, 1.0]), 0.25 * pi, 640, 480)
renderer = Renderer(camera)
lightsource = array([0.0, 0.0, 10.0])
objects = []

properties = Properties(array([1.0, 0.0, 0.0]))
objects.append(Sphere(array([5.0, 0.0, 1.0]), 1.0, properties))

renderer(lightsource, objects)
renderer.save_image("LaTeX/images/example1.png")
