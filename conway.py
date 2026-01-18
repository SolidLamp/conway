import numpy as np
from numpy._typing import NDArray


def copyArray(array: NDArray):
  h = array.shape[0]
  w = array.shape[1]
  new_array = np.zeros((h, w))
  for x in range(w):
    for y in range(h):
      new_array[x, y] = array[x, y]
  return new_array


def ReturnCoords(settings: dict, coord: tuple, array: NDArray):
  x = coord[0]
  y = coord[1]
  rows = array.shape[0]
  cols = array.shape[1]
  wrap = settings['wrap']
  if (x < 0 or x > (rows - 1)) and wrap:
    x = x % rows
  if (y < 0 or y > (cols - 1)) and wrap:
    y = y % cols
  if (x != x % rows or y != y % cols) and not wrap:
    return -1, -1
  return x, y


def detectNeighbours(settings: dict, array: NDArray, x: int, y: int):
  coords = [(i, j) for i in [x - 1, x, x + 1] for j in [y - 1, y, y + 1]]
  neighbours = 0
  for coord in coords:
    xi, yi = ReturnCoords(settings, coord, array)
    if xi != -1 and yi != -1:
      neighbours += array[xi, yi]
  neighbours -= array[x, y]
  return neighbours


def conway(settings: dict, array: NDArray, x: int, y: int) -> int:
  neighbours = detectNeighbours(settings, array, x, y)
  match neighbours:
    case 0 | 1:
      return 0
    case 2:
      return array[x, y]
    case 3:
      return 1
    case _:
      return 0


def conwayPass(settings: dict, array: NDArray) -> NDArray:
  rows = array.shape[0]
  cols = array.shape[1]
  new_array = np.zeros((rows, cols))
  for x in range(rows):
    for y in range(cols):
      new_array[x, y] = conway(settings, array, x, y)
  return new_array
