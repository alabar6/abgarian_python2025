import numpy as np

from src.methods.bilinear import BilinearInterpolation
from src.utils.grid import RectangularGrid


def increase_size(image: np.ndarray, scale: tuple[int, int]) -> np.ndarray:
    """
    Increase size of ``image`` in ``scale`` times (each axes on eaxh scale) using bilinear interpolation.
    If ``image`` shape was (W, H) and ``scale`` = (N1, N2) then size of output image will be:

    ((W - 1) * N1 + 1, (H - 1) * N2 + 1)

    Parameters
    ----------

    image : np.ndarray

        Source image

    scale : tuple[int, int]

        Scale value

    Returns
    -------

    output : np.ndarray

        Resized image
    """

    scale_x, scale_y = scale
    w, h = image.shape

    new_shape = ((w - 1) * scale_x + 1, (h - 1) * scale_y + 1)

    x_new = scale_x * np.arange(0, w + 1)
    y_new = scale_y * np.arange(0, h + 1)

    grid = RectangularGrid(x_coords=x_new, y_coords=y_new)
    bi = BilinearInterpolation(grid=grid, values=image)

    output = np.zeros(new_shape)
    for i in range(new_shape[0]):
        for j in range(new_shape[1]):
            output[i][j] = bi((i, j))

    return output
