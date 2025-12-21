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
      i = i2 // 2
      for j2 in range(20):
        j = j2 // 2
        if array[j, i] == 0:
          win.addstr("  ")
        elif array[j, i] == 1:
          win.addstr("██")
      newline(win)
      win.refresh()

def main(win, array: NDArray):
  curses.curs_set(0)
  win.scrollok(True)
  curses.cbreak()
  win.clear()
  gen = 1
  while 1:
    win.addstr(f'Generation: {gen}')
    newline(win)
    drawArray(win, array)
    time.sleep(0.5)
    win.clear()
    array = conway.conwayPass(array)
    gen += 1


def gui(array):
  curses.wrapper(main, array)
