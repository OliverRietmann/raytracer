#!/usr/bin/python

from sys import argv

from numpy import array, pi

from core.camera import Camera
from core.renderer import Renderer
from core.properties import Properties

from object.box import Box
from object.plane import Plane
from object.sphere import Sphere

if len(argv) == 2:
    filename = str(argv[1])
else:
    filename = "image.png"

camera = Camera(array([-10.0, 0.0, 2.0]), array([0.0, 0.0, 1.0]), 0.25 * pi, 640, 480)

renderer = Renderer(camera)

lightsource_list = [array([0.0, 5.0, 10.0]), array([-5.0, 10.0, 5.0])]

object_list = []

red = array([1.0, 0.0, 0.0])
properties = Properties(color=red, ambient=0.2, diffuse=0.8)
object_list.append(Sphere(array([4.0, -2.0, 0.0]), 1.0, properties))

purple = array([148.0 / 255.0, 0.0, 211.0 / 255.0])
properties = Properties(color=purple, ambient=0.2, diffuse=0.2, phong=[1.0, 30], reflection=0.6)
object_list.append(Sphere(array([6.0, 2.0, 1.0]), 2.0, properties))

blue = array([0.0, 0.0, 1.0])
properties = Properties(color=blue, ambient=0.2, diffuse=0.8)
object_list.append(Box(array([-0.5, -3.0, -1.0]), array([0.5, -2.0, 0.0]), properties))

gray = array([0.7, 0.7, 0.7])
properties = Properties(color=gray, ambient=0.2, diffuse=0.6, phong=[0.0, 0], reflection=0.2)
object_list.append(Plane(array([0.0, 0.0, 1.0]), 1.0, properties))

renderer(lightsource_list, object_list)
renderer.save_image(filename)
