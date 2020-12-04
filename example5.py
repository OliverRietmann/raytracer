from numpy import array, pi

from core.camera import Camera
from core.renderer import Renderer
from object.box import Box
from object.plane import Plane
from object.sphere import Sphere

camera = Camera(array([-7.5, -4.3, 3.0]), array([0.0, 0.0, 1.0]), 0.25 * pi, 640, 480)
renderer = Renderer(camera)

lightsource = array([1.0, -7.0, 10.0])

black = array([0.0, 0.0, 0.0])
white = array([1.0, 1.0, 1.0])
gray = array([0.8, 0.8, 0.8])

dx = 1.0
dy = 1.0

box_list = []
n = 10
for i in range(n):
    x = dx * (n / 2 - i)
    for j in range(n):
        y = dy * (n / 2 - j)
        if (i + j) % 2 == 0:
            color = black
        else:
            color = white
        p = array([x, y, -1.0])
        q = array([x + dx, y + dy, 0.0])
        box = Box(p, q, color=color, ambient=1.0)
        box_list += [box]

plane1 = Plane(array([-1.0, 0.0, 0.0]), 6.0, color=gray, ambient=0.2, diffuse=0.8)
plane2 = Plane(array([0.0, -1.0, 0.0]), 6.0, color=gray, ambient=0.2, diffuse=0.8)
plane3 = Plane(array([1.0, 0.0, 0.0]), 5.0, color=gray, ambient=0.2, diffuse=0.8)
plane4 = Plane(array([0.0, 1.0, 0.0]), 5.0, color=gray, ambient=0.2, diffuse=0.8)
plane_list = [plane1, plane2, plane3, plane4]

sphere = Sphere(array([2.0, 2.0, 1.0]), 1, color=white, ambient=0.0, reflection=1.0)
sphere_list = [sphere]

renderer([lightsource], box_list + plane_list + sphere_list)
renderer.save_image("example5.png")
