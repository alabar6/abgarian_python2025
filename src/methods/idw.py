import numpy as np

from src.utils.grid import RectangularGrid


class InverseDistanceWeighting:
    """Implementation of inverse distance weighting on rectangular grid.

    :param grid: Values of new grid defined on old grid
    :type grid: RectangularGrid

    :param values: Values of function defined on old grid
    :type values: np.ndarray

    :param p: value used in interpolation formula. The default is 1
    :type p: int, optional
    """

    def __init__(self, grid: RectangularGrid, values: np.ndarray, p: int = 4):
        """Constructor method"""

        self.grid = grid
        self.p = p
        self.values = values

    def calculate_weights(
        self,
        point: tuple[float, float],
    ) -> float:
        """
        Calculate weights map of ``point``

        Parameters
        ----------
        point : tuple[float, float]

            A source point to interpolation

        Returns
        -------
        predict : float

            Interpolated value in point (x, y)

        """
        meshgrid = self.grid.meshgrid()
        x, y = point

        distances = np.zeros(meshgrid[0].shape)

        where_x = np.where(self.grid.x_coords == x)[0]
        where_y = np.where(self.grid.y_coords == y)[0]

        if (len(where_x) != 0) and (len(where_y) != 0):
            distances[where_y[0], where_x[0]] = 1
            return np.transpose(distances)
        
        x, y = point
        distances = np.sqrt(np.square(x - meshgrid[0]) + np.square(y - meshgrid[1]))

        weights = np.power(distances, -self.p)

        return np.transpose(weights)

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

        weights = self.calculate_weights(point)
        return np.sum(weights * self.values) / np.sum(weights)
