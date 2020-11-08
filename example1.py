from numpy import array, pi

from core.camera import Camera
from core.renderer import Renderer
from myobject.sphere import Sphere

# Platziere eine Kamera im Punkt [-1.0, 0.0, 1.0] welche in Richtung
# des Punktes [0.0, 0.0, 1.0] schaut.
camera = Camera(array([-1.0, 0.0, 1.0]), array([0.0, 0.0, 1.0]), 0.25 * pi, 640, 480)

# Renderer ist eine Klasse zum Generieren der Bilder
renderer = Renderer(camera)

# Eine Kugel um [5.0, 0.0, 1.0] mit Radius 1 (in der Farbe rot)
sphere = Sphere(array([5.0, 0.0, 1.0]), 1.0)

# Man übergiebt dem Renderer eine Liste von Objekten (die Kugel)
renderer([], [sphere], photo_exposure=0.0)

# Hier wird das Bild generiert und abgespeichert
renderer.save_image("example1.png")
