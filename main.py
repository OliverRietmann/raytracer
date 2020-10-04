from numpy import array, pi
from core.camera import Camera
from core.renderer import Renderer
from core.ray import Ray

from object.sphere import Sphere

camera = Camera(array([-1.0, 0.0, 0.0]), array([0.0, 0.0, 0.0]), 0.25 * pi, 640, 480)
renderer = Renderer(camera)
sphere = Sphere(array([5.0, 0.0, 0.0]), 1.0)
#ray = Ray(array([-1.0, 0.0, 0.0]), array([1.0, 0.0, 0.0]))
#print(sphere.intersect(ray))
renderer(sphere)
renderer.save_image("image.png")
