import numpy as np

#array = np.zeros((10, 10))
array = np.random.randint(0, 2, size=(10, 10))
#array[9, 9] = 1
#array[0, 9] = 2
#array[1, 9] = 3
#array[1, 0] = 4
#array[1, 1] = 5
#array[0, 1] = 6
#array[9, 1] = 7
#array[9, 0] = 8

def copyArray(array):
  new_array = np.zeros((10, 10))
  for x in range(10):
    for y in range(10):
      new_array[x, y] = array[x, y]
  return new_array

def ReturnCoords(coord: tuple):
  x = coord[0]
  y = coord[1]
  if x < 0 or x > 9:
    x = x % 10
  if y < 0 or y > 9:
    y = y % 10
  return x, y

def detectNeighbour(array, x, y):
  return array[x, y]

def detectNeighbours(array, x, y):       # (-1, 1)   (0, 1)   (1, 1)
  #xi, yi = ReturnCoords((x - 1, y + 1))  # (-1, 0)   (0, 0)   (1, 0)
                                         # (-1, -1)  (0, -1)  (1, -1)
  coords = [(i, j) for i in [x - 1, x, x + 1] for j in [y - 1, y, y + 1]]
  neighbours = 0
  for coord in coords:
    xi, yi = ReturnCoords(coord)
    print(coord, xi, yi)
    print(array[xi, yi])
    neighbours += array[xi, yi]
  neighbours -= array[x, y]
  return neighbours

def conway(array, x, y):
  neighbours = detectNeighbours(array, x, y)
  match neighbours:
    case 0 | 1:
      return 0
    case 2:
      return array[x, y]
    case 3:
      return 1
    case _:
      return 0

def conwayPass(array):
  new_array = np.zeros((10, 10))
  for x in range(10):
    for y in range(10):
      new_array[x, y] = conway(array, x, y)
      #new_array[x + 1, y + 1] = array[x, y]
  return new_array

print(array)
array = conwayPass(array)
print(array)
#print(detectNeighbours(array, 0, 0))
