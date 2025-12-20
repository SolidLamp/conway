import curses
import time
import numpy as np
import conway
import cursesui
import seed

if __name__ == "__notmain__":
  array = np.random.randint(0, 2, size=(10, 10))
  array = np.zeros((10, 10))
  array[1, 1] = 1
  array[2, 2] = 1
  array[3, 1] = 1
  array[3, 2] = 1
  array[2, 3] = 1
  print(array)

  #
   ##
  ##

  for i in range(100):
    print(array)
    time.sleep(0.1)
    array = conway.conwayPass(array)


if __name__ == "__main__":
  array = np.random.randint(0, 2, size=(10, 10))
  cursesui.gui(array)
