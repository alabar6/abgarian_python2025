import numpy as np

from src.utils.grid import RectangularGrid


class BilinearInterpolation:
    """
    Implementation of bilinear interpolation on rectangular grid

    :param grid: Values of new grid defined on old grid
    :type grid: RectangularGrid

    :param values: Values of function defined on old grid
    :type values: np.ndarray
    """

    def __init__(self, grid: RectangularGrid, values: np.ndarray):
        """Constructor method"""

        self.grid = grid
        self.values = values

    def find_nearest(self, point: tuple[float, float]) -> tuple[int, int, int, int]:
        """
        Return list of indices of 4 points on grid that are close to source ``point``

        Parameters
        ----------
        point: tuple[float, float]

            Coordinates of point on new grid

        Returns
        -------
        indices: tuple[int, int, int, int]

            Indices of x and y chords of points that are close to source ``point``
        """

        array_x = self.grid.x_coords
        array_y = self.grid.y_coords

        x, y = point

        i = np.searchsorted(array_x, x)
        j = np.searchsorted(array_y, y)

        return i - 1, i, j - 1, j

    def bilinear(
        self,
        point: tuple[float, float],
        x_points: tuple[int, int],
        y_points: tuple[int, int],
    ) -> float:
        """
        Makes bilinear interpolation for ``point`` :math:`(x, y)` on rectangle with vertexes :math:`(x_1, y_1), (x_1, y_2),
        (x_2, y_1), (x_2, y_2)`, where :math:`x_1, x_2, y_1, y_2` are values of new grid, defined on old grid with
        indices in arrays ``x_points`` and ``y_points``

        Parameters
        ----------
        point : tuple[float, float]

            A source point to interpolation

        x_points : tuple[float, float]

            An array of two x-coordinates of rectangle

        y_points : tuple[float, float]

            An array of two y-coordinates of rectangle

        Returns
        -------
        predict : float

            Interpolated value in point (x, y)

        Examples
        --------
        >>> grid = RectangularGrid(x_coords=[0, 2], y_coords=[0, 2])
        >>> val = [[0, 1], 
        >>>        [1, 2]]
        >>> bi = BilinearInterpolation(grid=grid, values=val)
        >>> bi.bilinear((1, 1), (0, 2), (0, 2))
        1
        """

        x, y = point

        x1_idx, x2_idx = x_points
        y1_idx, y2_idx = y_points

        x1, x2 = self.grid.x_coords[x1_idx], self.grid.x_coords[x2_idx]
        y1, y2 = self.grid.y_coords[y1_idx], self.grid.y_coords[y2_idx]

        f11 = self.values[x1_idx][y1_idx]
        f12 = self.values[x1_idx][y2_idx]
        f21 = self.values[x2_idx][y1_idx]
        f22 = self.values[x2_idx][y2_idx]

        den = (x2 - x1) * (y2 - y1)

        sum11 = f11 * (x2 - x) * (y2 - y) / den
        sum21 = f21 * (x - x1) * (y2 - y) / den
        sum12 = f12 * (x2 - x) * (y - y1) / den
        sum22 = f22 * (x - x1) * (y - y1) / den

        return sum11 + sum12 + sum21 + sum22

    def __call__(self, point: tuple[float, float]) -> float:
        """
        Make interpolation in ``point`` on new grid

        Parameters
        ----------

        point : point: tuple[float, float]

            Point on new grid

        Returns
        -------
        predict : float

            Interpolated value in point (x, y)
        """

        indices = self.find_nearest(point)
        return self.bilinear(point, indices[0:2], indices[2:4])
