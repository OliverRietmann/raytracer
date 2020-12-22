from sys import argv

from numpy import array, pi

from core.camera import Camera
from core.renderer import Renderer

from object.box import Box
from object.plane import Plane
from object.sphere import Sphere

if len(argv) == 2:
    filename = str(argv[1])
else:
    filename = "image.png"

camera = Camera(array([-10.0, 0.0, 2.0]), array([0.0, 0.0, 1.0]), 0.25 * pi, 640, 480)
renderer = Renderer(camera)

red = array([1.0, 0.0, 0.0])
sphere_red = Sphere(array([4.0, -2.0, 0.0]), 1.0, color=red, ambient=0.2, diffuse=0.8)

purple = array([148.0 / 255.0, 0.0, 211.0 / 255.0])
sphere_purple = Sphere(array([6.0, 2.0, 1.0]), 2.0,
                color=purple, ambient=0.2, diffuse=0.2, reflection=0.6)

blue = array([0.0, 0.0, 1.0])
box_blue = Box(array([-0.5, -3.0, -1.0]), array([0.5, -2.0, 0.0]),
                color=blue, ambient=0.2, diffuse=0.8)

gray = array([0.7, 0.7, 0.7])
plane_gray = Plane(array([0.0, 0.0, 1.0]), 1.0, color=gray, ambient=0.2, diffuse=0.6,
                reflection=0.2)

lightsource_list = [array([0.0, 5.0, 10.0]), array([-5.0, 10.0, 5.0])]
object_list = [sphere_red, sphere_purple, box_blue, plane_gray]
renderer(lightsource_list, object_list)
renderer.save_image(filename)
