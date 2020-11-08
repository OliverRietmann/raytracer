from numpy import array, pi

from core.camera import Camera
from core.renderer import Renderer
from object.sphere import Sphere

camera = Camera(array([-1.0, 0.0, 1.0]), array([0.0, 0.0, 1.0]), 0.25 * pi, 640, 480)
renderer = Renderer(camera)

lightsource = array([0.0, 0.0, 10.0])

sphere = Sphere(array([5.0, 0.0, 1.0]), 1.0, ambient=0.0, diffuse=1.0)

renderer([lightsource], [sphere], 0.0)
renderer.save_image("example2.png")
