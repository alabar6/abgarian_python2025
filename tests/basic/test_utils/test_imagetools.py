"""Test imagetools methods"""

import numpy as np
import pytest

from src.utils.imagetools import plot_images, read_image


@pytest.fixture
def read_cat_image():
    img = read_image(path="./src/data/cat.png")
    return img


def test_read_image_is_npndarray(read_cat_image):
    """Image must have ``np.ndarray`` data type"""

    assert isinstance(read_cat_image, np.ndarray)


def test_read_gray_image_correct_shape(read_cat_image):
    """Gray image after reading must have shape (h, w)"""
    correct_shape = (225, 300)

    assert read_cat_image.shape == correct_shape


def test_read_rgb_image_correct_shape():
    """RGB image after reading must have shape (3, h, w)"""
    img = read_image(path="./src/data/cat.png", rgb=True)
    correct_shape = (225, 300, 3)

    assert img.shape == correct_shape


def test_read_image_correctly_changed_shape():
    """Check that shape of image changes correctly"""
    new_shape = (200, 200)
    img = read_image(path="./src/data/cat.png", shape=new_shape)

    assert img.shape == new_shape


def test_read_image_to_float_correct_pixel_value():
    """After reading the image with the modifier ``to_float``=True, the pixel values should be in the range [0, 1]"""
    img = read_image(path="./src/data/cat.png", to_float=True)

    assert np.all(img >= 0) and np.all(img <= 1)


def test_plot_images_incorrect_titles_length(read_cat_image):
    """Length of ``images`` and ``titles`` arrays must be same"""

    images = [read_cat_image]
    titles = ["a", "b"]

    with pytest.raises(AssertionError):
        plot_images(images, titles)


def test_plot_images_cant_save_without_title(read_cat_image):
    """Output image can't be saved without title"""

    images = [read_cat_image]
    save_dir = "./src/data/"

    with pytest.raises(AssertionError):
        plot_images(images, save_dir=save_dir)
