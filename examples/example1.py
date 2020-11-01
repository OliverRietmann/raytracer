#export PYTHONPATH="${PYTHONPATH}:/path/to/top/directory"

from numpy import array, pi
from core.camera import Camera
from core.renderer import Renderer
from core.properties import Properties

from object.sphere import Sphere

camera = Camera(array([-1.0, 0.0, 1.0]), array([0.0, 0.0, 1.0]), 0.25 * pi, 640, 480)
renderer = Renderer(camera)
lightsource_list = [array([0.0, 0.0, 10.0])]

object_list = []

properties = Properties(color=array([1.0, 0.0, 0.0]))
object_list.append(Sphere(array([5.0, 0.0, 1.0]), 1.0, properties))

renderer(lightsource_list, object_list, 0.0)
renderer.save_image("LaTeX/images/example1.png")
