import curses
import numpy as np
import cursesui
import seed

if __name__ == "__main__":
  array = np.random.randint(0, 2, size=(10, 10))
  array = curses.wrapper(seed.main)
  cursesui.gui(array)
