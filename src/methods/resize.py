import numpy as np

from src.methods.bilinear import BilinearInterpolation
from src.methods.idw import InverseDistanceWeighting
from src.utils.grid import RectangularGrid


def increase_size(image: np.ndarray, scale: tuple[int, int]) -> np.ndarray:
    """
    Increase size of ``image`` in ``scale`` times (each axes on eaxh scale) using bilinear interpolation.
    If ``image`` shape was :math:`(W, H)` and ``scale`` = :math:`(N_1, N_2)` then size of output image will be:

    $$
    ((W - 1) N_1 + 1, (H - 1) N_2 + 1)
    $$

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

def increase_size_idw(image: np.ndarray, scale: tuple[int, int], p: int = 1) -> np.ndarray:
    """
    Increase size of ``image`` in ``scale`` times (each axes on eaxh scale) using inverse distance weighting.
    If ``image`` shape was :math:`(W, H)` and ``scale`` = :math:`(N_1, N_2)` then size of output image will be:

    $$
    ((W - 1) N_1 + 1, (H - 1) N_2 + 1)
    $$

    Parameters
    ----------

    image : np.ndarray

        Source image

    scale : tuple[int, int]

        Scale value

    p : int, optional

        Parameter of inverse distance weighting algorithm

    Returns
    -------

    output : np.ndarray

        Resized image
    """

    scale_x, scale_y = scale
    w, h = image.shape

    new_shape = ((w - 1) * scale_x + 1, (h - 1) * scale_y + 1)

    x_new = scale_x * np.arange(0, w)
    y_new = scale_y * np.arange(0, h)

    grid = RectangularGrid(x_coords=x_new, y_coords=y_new)
    idw = InverseDistanceWeighting(grid=grid, values=image)

    output = np.zeros(new_shape)
    for i in range(new_shape[0]):
        for j in range(new_shape[1]):
            output[i][j] = idw((i, j))

    return output
