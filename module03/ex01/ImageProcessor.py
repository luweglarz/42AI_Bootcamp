import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

class ImageProcessor:
    def load(self, path):
        im = Image.open(path)
        img = mpimg.imread(path)
        weight, height = im.size
        print("Loading an image of dimension", height, weight)
        return np.array(img)
    def display(self, array):
        imgplot = plt.imshow(array)
        plt.show()
        