import click

from src.methods.resize import increase_size
from src.utils.imagetools import plot_images, read_image


@click.command()
@click.option("--image_dir", default = "./src/data/cat.png", help = "Directory of image")
@click.option("--method", default = "bilinear", help = "Method of interpolation")
@click.option("--scale_x", default = 1, help = "Axes x resize parameter")
@click.option("--scale_y", default = 1, help = "Axes y resize parameter")
def demo(image_dir, method, scale_x, scale_y):
    scale = (scale_x, scale_y)

    img = read_image(
        path=image_dir,
        to_float=True,
    )

    if method == "bilinear": 
        new_image = increase_size(img, scale)
        plot_images(images=[img, new_image], titles=["Original", "Resized via bilinear interpolation"])


if __name__ == "__main__":
    demo()
