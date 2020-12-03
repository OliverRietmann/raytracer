from numpy import array, pi

from core.camera import Camera
from core.renderer import Renderer
from myobject.box import Box
from myobject.plane import Plane

camera = Camera(array([-1.0, -3.5, 3.0]), array([5.0, 0.0, 1.0]), 0.25 * pi, 640, 480)
renderer = Renderer(camera)

lightsource = array([1.0, -8.0, 10.0])

white = array([1.0, 1.0, 1.0])
red = array([1.0, 0.0, 0.0])
green = array([0.0, 1.0, 0.0])
blue = array([0.0, 0.0, 1.0])

d = array([1.0, 1.0, 1.0])
pr = array([6.0, -2.0, 0.0])
pg = array([5.0, -0.5, 0.0])
pb = array([4.0, 1.0, 0.0])

box_red = Box(pr, pr + d, color=red, ambient=0.2, diffuse=0.8)
box_green = Box(pg, pg + d, color=green, ambient=0.2, diffuse=0.8)
box_blue = Box(pb, pb + d, color=blue, ambient=0.2, diffuse=0.8)

plane = Plane(array([0.0, 0.0, 1.0]), 0.0, color=white, ambient=0.2, diffuse=0.8)

renderer([lightsource], [box_red, box_green, box_blue, plane], 0.0)
renderer.save_image("example4.png")
