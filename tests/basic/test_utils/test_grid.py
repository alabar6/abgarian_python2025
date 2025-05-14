"""Test grid methods"""

import numpy as np
import pytest

from src.utils.grid import RectangularGrid, EquidistGrid

@pytest.fixture
def correct_meshgrid():
    x_correct_meshgrid = [[0, 1, 2],
                          [0, 1, 2],
                          [0, 1, 2]]
    
    y_correct_meshgrid = [[0, 0, 0],
                          [1, 1, 1],
                          [2, 2, 2]]
    return x_correct_meshgrid, y_correct_meshgrid

def test_rectangular_grid_make_correct_meshgrid(correct_meshgrid):
    """Meshgrid method must make correct meshgrid"""

    x_coords = [0, 1, 2]
    y_coords = [0, 1, 2]
    
    grid = RectangularGrid(x_coords=x_coords, y_coords=y_coords)
    out_meshgrid = grid.meshgrid()

    assert np.all(out_meshgrid[0] == correct_meshgrid[0]), np.all(out_meshgrid[1] == correct_meshgrid[1])

def test_equidist_grid_make_correct_meshgrid(correct_meshgrid):
    """Meshgrid method must make correct meshgrid"""

    grid = EquidistGrid(corners = [(0, 0), (3, 3)], gap = 1)
    out_meshgrid = grid.meshgrid()

    assert np.all(out_meshgrid[0] == correct_meshgrid[0]), np.all(out_meshgrid[1] == correct_meshgrid[1])