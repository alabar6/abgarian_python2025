import numpy as np

class Grid:
  """
  Mother Grid class
  """
  pass
                                                    
class RectangularGrid:
  """
  Makes a rectangular grid with given x, y coordinates
  """

  def __init__(self,
               x_coords: np.ndarray,
               y_coords: np.ndarray):
    
    self.x_coords = x_coords
    self.y_coords = y_coords

  def meshgrid(self):       
    return np.meshgrid(self.x_coords, self.y_coords)
  
class EquidistGrid(RectangularGrid):
  """
  Makes a rectangular grid with fixed gap between points
  """

  def __init__(self,
               corners: tuple[np.ndarray, np.ndarray],
               gap):

    self.x_coords = np.arange(corners[0][0], corners[1][0], step = gap)
    self.y_coords = np.arange(corners[0][1], corners[1][1], step = gap)
