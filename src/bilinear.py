import numpy as np
from utils.basis import linear_basis
from utils.grid import RectangularGrid

class BilinearInterpolation:
  """
  Implementation of bilinear interpolation on rectangular grid
  """

  def __init__(self,
               grid: RectangularGrid,
               values: np.ndarray):
    
    self.grid = grid
    self.values = values

  def _find_nearest(self, coords):
    """
    Return list of 4 points on grid,  
    """
    array_x = self.grid.x_coords
    array_y = self.grid.y_coords

  def _value(self, point):
    x, y = point

    array_x = self.grid.x_coords
    array_y = self.grid.y_coords

    i = np.where(array_x = x)
    j = np.where(array_y = y)

    assert np.size(i) == 1 and np.size(j) == 1, "Grid or point is set incorrectly"

    

    

  def _bilinear(self, x_points, y_points):
    """
    
    """

    x1, x2 = x_points
    y1, y2 = y_points


    

  def __call__(x):