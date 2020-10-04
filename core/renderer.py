from numpy import array, inf, zeros
from numpy.random import rand
from matplotlib.pyplot import figure, imshow, savefig, subplots_adjust

class Renderer:
    def __init__(self, camera):
        self.camera = camera
        self.rgb_data = zeros((camera.pixels_y, camera.pixels_x, 3), dtype=float)
        #self.rgb_data = rand(camera.pixels_y, camera.pixels_x, 3)

    def __call__(self, objects):
        for ray, i, j in self.camera.get_ray_indices():
            t = objects.intersect(ray)
            if (t < inf):
                self.rgb_data[i, j] = objects.color

    def save_image(self, filename):
        x = self.camera.pixels_x
        y = self.camera.pixels_y
        fig = figure(figsize=(1, y / x))
        imshow(self.rgb_data, aspect='equal', interpolation='none')
        subplots_adjust(left=0, right=1, bottom=0, top=1)
        savefig(filename, dpi=x)
