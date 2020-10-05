from numpy import array, cross, tan
from numpy.linalg import norm

from core.ray import Ray

def normalize(vector):
    return vector / norm(vector)

class Camera:
    def __init__(self, position, look_at, angle, pixels_x, pixels_y):
        self.position = position
        self.look_at = look_at
        self.angle = angle
        self.pixels_x = pixels_x
        self.pixels_y = pixels_y

    def get_ray_indices(self):
        direction = normalize(self.look_at - self.position)
        w = normalize(cross(direction, array([0.0, 0.0, 1.0])))
        h = cross(direction, w)
        pixelsize = 2.0 * tan(0.5 * self.angle) / self.pixels_x;
        
        for i in range(self.pixels_y):
            dy = (i - 0.5 * (self.pixels_y - 1)) * pixelsize * h
            for j in range(self.pixels_x):
                dx = (j - 0.5 * (self.pixels_x - 1)) * pixelsize * w
                yield (Ray(self.position, direction + dx + dy), i, j)
