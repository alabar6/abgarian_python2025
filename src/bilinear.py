import numpy as np
from utils.grid import RectangularGrid

class BilinearInterpolation:
  """
  Implementation of bilinear interpolation on rectangular grid
  """

  def __init__(self,
               grid: RectangularGrid,
               values: np.ndarray):
    """
    Parameters:
    -----------
    grid: RectangularGrid
          Values of new grid defined on old grid
    values: np.ndarray
            Values of function defined on old grid
    """
    self.grid = grid
    self.values = values

  def _find_nearest(self, 
                    point: tuple[float, float]) -> tuple[int, int, int, int]:
    """
    Return list of 4 points on grid that a close to source point

    Parameters
    ----------
      point: tuple[float, float]
      
      Coordinates of point on new grid
    """
  
    array_x = self.grid.x_coords
    array_y = self.grid.y_coords

    x, y = point

    i = np.searchsorted(array_x, x)
    j = np.searchsorted(array_y, y)

    # if i == 0 and j == 0:
    #   return i, i + 1, j, j + 1
    
    # if i == 0:
    #   return i, i + 1, j - 1, j
    
    # if i == 0 and j == 0:
    #   return i - 1, i, j, j + 1

    return i - 1, i, j - 1, j

  # def _value(self, point):
  #   x, y = point

  #   array_x = self.grid.x_coords
  #   array_y = self.grid.y_coords

  #   i = np.where(array_x = x)
  #   j = np.where(array_y = y)

  #   assert np.size(i) == 1 and np.size(j) == 1, "Grid or point is set incorrectly"

  #   return self.values[i.item()][j.item()]  
    

  # def bilinear(self, 
  #               point: tuple[float, float], 
  #               x_points: tuple[float, float], 
  #               y_points: tuple[float, float]):
  #   """
  #   Makes bilinear interpolation for point (x, y) on rectangle with vertexes (x1, y1), (x1, y2), 
  #   (x2, y1), (x2, y2), where x1, x2 = x_points; y1, y2 = y_points

  #   Parameters:
  #   -----------
  #   point: tuple[float, float]
  #          A source point to interpolation

  #   x_points: tuple[float, float]
  #          An array of two x-coordinates of rectangle

  #   y_points: tuple[float, float]
  #          An array of two y-coordinates of rectangle
  #   """

  #   x, y = point
  #   x1, x2 = x_points
  #   y1, y2 = y_points

  #   f11 = self._value((x1, y1))
  #   f12 = self._value((x1, y2))
  #   f21 = self._value((x2, y1))
  #   f22 = self._value((x2, y2))

  #   den = (x2 - x1) * (y2 - y1)

  #   sum11 = f11 * (x2 - x) * (y2 - y) / den
  #   sum21 = f21 * (x - x1) * (y2 - y) / den
  #   sum12 = f12 * (x2 - x) * (y - y1) / den
  #   sum22 = f22 * (x - x1) * (y - y1) / den

  #   return sum11 + sum12 + sum21 + sum22
  
  def _bilinear(self, 
                point: tuple[float, float], 
                x_points: tuple[int, int], 
                y_points: tuple[int, int]) -> float:
    """
    Makes bilinear interpolation for ``point`` (x, y) on rectangle with vertexes (x1, y1), (x1, y2), 
    (x2, y1), (x2, y2), where x1, x2, y1, y2 are values of new grid, defined on old grid with
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
    

  def __call__(self, 
               point: tuple[float, float]) -> float:    
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

    indices = self._find_nearest(point)
    # print(indices)
    return self._bilinear(point, indices[0:2], indices[2:4])

