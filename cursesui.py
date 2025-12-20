import curses
import math
import time
import numpy as np
from numpy._typing import NDArray
import conway

def newline(win):
  max_y, max_x = win.getmaxyx()
  y, x = win.getyx()
  y += 1
  x = 0
  if y >= max_y:
    win.scroll()
    y = max_y - 1
  if y >= max_y - 1:
    win.move(max_y - 1, x)
  else:
    win.move(y, x)
  win.refresh()

def drawArray(win, array: NDArray):
  for i2 in range(20):
    i = math.floor(i2 / 2)
    for j2 in range(20):
      j = math.floor(j2 / 2)
      if array[j, i] == 0:
        win.addstr("   ")
      elif array[j, i] == 1:
        win.addstr(" █ ")
      #coords = str(i) + "," + str(j)
      #win.addstr(coords)
    time.sleep(0.01)
    newline(win)
    win.refresh()

def main(win):
  curses.curs_set(0)
  win.scrollok(True)
  curses.cbreak()
  win.addstr("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
  win.clear()
  array = np.random.randint(0, 2, size=(10, 10))
  #array = np.ones((10, 10))
  while 1:
    drawArray(win, array)
    time.sleep(0.5)
    win.clear()
    nArray = conway.conwayPass(array)
    array = nArray
    del nArray


def gui():
  curses.wrapper(main)
