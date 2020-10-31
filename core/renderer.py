from numpy import exp, ones_like, zeros
#from numpy.random import rand
from matplotlib.pyplot import figure, imshow, savefig, subplots_adjust

from core.tracer import get_nearest_obstacle

class Renderer:
    def __init__(self, camera):
        self.camera = camera
        self.rgb_data = zeros((camera.pixels_y, camera.pixels_x, 3), dtype=float)
        #self.rgb_data = rand(camera.pixels_y, camera.pixels_x, 3)

    def __call__(self, lightsource_list, object_list, photo_exposure=1.0):
        for ray, i, j in self.camera.get_ray_indices():
            obj, t = get_nearest_obstacle(ray, object_list)
            if obj is not None:
                self.rgb_data[i, j] = obj.shader(ray(t), ray.direction, lightsource_list, object_list)
                #if max(self.rgb_data[i, j]) > 1.0 or min(self.rgb_data[i, j]) < 0.0:
                #    print(self.rgb_data[i, j], i, j)
        if photo_exposure > 0.0:
            self.rgb_data[:, :] = ones_like(self.rgb_data[:, :]) - exp(-self.rgb_data[:, :] * photo_exposure)

    def save_image(self, filename):
        x = self.camera.pixels_x
        y = self.camera.pixels_y
        fig = figure(figsize=(1, y / x))
        imshow(self.rgb_data, aspect='equal', interpolation='none')
        subplots_adjust(left=0, right=1, bottom=0, top=1)
        savefig(filename, dpi=x)
