from numpy import array, pi

from core.camera import Camera
from core.renderer import Renderer
from myobject.box import Box
from myobject.plane import Plane
from myobject.sphere import Sphere

camera = Camera(array([-7.5, -4.3, 3.0]), array([0.0, 0.0, 1.0]), 0.25 * pi, 640, 480)
renderer = Renderer(camera)

lightsource = array([0.0, 0.0, 10.0])

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

kwargs = {'color': gray, 'ambient': 0.2, 'diffuse': 0.8}
plane1 = Plane(array([-1.0, 0.0, 0.0]), 6.0, **kwargs)
plane2 = Plane(array([0.0, -1.0, 0.0]), 6.0, **kwargs)
plane3 = Plane(array([1.0, 0.0, 0.0]), 5.0, **kwargs)
plane4 = Plane(array([0.0, 1.0, 0.0]), 5.0, **kwargs)
plane5 = Plane(array([0.0, 0.0, -1.0]), 12.0, **kwargs)
plane_list = [plane1, plane2, plane3, plane4, plane5]

kwargs = {'color': white, 'ambient': 0.0, 'reflection': 1.0}
sphere1 = Sphere(array([0.0, 2.0, 1.0]), 1, **kwargs)
sphere2 = Sphere(array([0.0, -2.0, 1.0]), 1, **kwargs)
sphere_list = [sphere1, sphere2]

renderer([lightsource], box_list + plane_list + sphere_list, 3.0)
renderer.save_image("example5.png")
