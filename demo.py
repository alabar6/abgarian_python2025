import numpy as np
import cv2
import matplotlib.pyplot as plt
from utils.imagetools import read_image, plot_images
from src.resize import increase_size


def demo():
    img = read_image(
        path="C:/Users/user/Desktop/interpolation/abgarian_python2025/data/cat.png",
        to_float=True,
    )

    new_image = increase_size(img, (2, 2))

    plot_images([img, new_image])


if __name__ == "__main__":
    demo()
