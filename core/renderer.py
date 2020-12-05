from numpy import exp, ones_like, uint8, zeros

from PIL.Image import fromarray

from core.tracer import get_nearest_obstacle

class Renderer:
    def __init__(self, camera):
        self.camera = camera
        self.rgb_data = zeros((camera.pixels_y, camera.pixels_x, 3), dtype=float)

    def __call__(self, lightsource_list, object_list, photo_exposure=1.0):
        for v, w, i, j in self.camera.get_ray_indices():
            obj, t = get_nearest_obstacle(v, w, object_list)
            if obj is not None:
                self.rgb_data[i, j] = obj.shader(v + t * w, w, lightsource_list, object_list)
        if photo_exposure > 0.0:
            self.rgb_data[:, :] = ones_like(self.rgb_data[:, :]) - exp(-self.rgb_data[:, :] * photo_exposure)

    def save_image(self, filename):
        fromarray((self.rgb_data * 255).astype(uint8), 'RGB').save(filename)
