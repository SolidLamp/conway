import curses
import math
import time
import numpy as np
from numpy._typing import NDArray
import conway

def newline(win, num = 1):
  max_y, max_x = win.getmaxyx()
  y, x = win.getyx()
  y += num
  x = 0
  if y >= max_y:
    win.scroll()
    y = max_y - num
  if y >= max_y - num:
    win.move(max_y - num, x)
  else:
    win.move(y, x)
  win.refresh()

def drawArray(win, array: NDArray):
  if array.shape[0] > 15 or array.shape[1] > 15:
    for i in range(array.shape[0]):
      for j in range(array.shape[1]):
        if array[j, i] == 0:
          win.addstr(" ")
        elif array[j, i] == 1:
          win.addstr("█")
      newline(win)
      win.refresh()
  else:
    for i2 in range(20):
      i = math.floor(i2 / 2)
      for j2 in range(20):
        j = math.floor(j2 / 2)
        if array[j, i] == 0:
          win.addstr("  ")
        elif array[j, i] == 1:
          win.addstr("██")
        #coords = str(i) + "," + str(j)
        #win.addstr(coords)
      newline(win)
      win.refresh()

def main(win, array: NDArray):
  curses.curs_set(0)
  win.scrollok(True)
  curses.cbreak()
  win.addstr("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
  win.clear()
  #array = np.random.randint(0, 2, size=(10, 10))
  #array = np.ones((10, 10))
  gen = 1
  while 1:
    win.addstr(f'Generation: {gen}')
    newline(win)
    drawArray(win, array)
    time.sleep(0.5)
    win.clear()
    nArray = conway.conwayPass(array)
    array = nArray
    del nArray
    gen += 1


def gui(array):
  curses.wrapper(main, array)
