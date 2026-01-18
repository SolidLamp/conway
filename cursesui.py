import curses
import time
import numpy as np
from numpy._typing import NDArray
import conway

__maxsmall__ = 10
__mindelay__ = 0.001

def wait(win: curses.window, interval: float, mindelay: float = __mindelay__) -> bool:
  """time.sleep with an interrupt
     this code is bad but works"""
  if isinstance(interval, int):
    interval = float(interval)
  if interval < 0:
    interval = 0
  win.nodelay(True)
  key = win.getch()
  while interval > 0 and key == -1:
    time.sleep(min(mindelay, interval))
    interval -= min(mindelay, interval)
    key = win.getch()
  win.nodelay(False)
  if key == -1:
    return False
  else:
    return True

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
  if array.shape[0] > __maxsmall__ or array.shape[1] > __maxsmall__:
    for i in range(array.shape[1]):
      for j in range(array.shape[0]):
        if array[j, i] == 0:
          win.addstr(" ")
        elif array[j, i] == 1:
          win.addstr("█")
      newline(win)
      win.refresh()
  else:
    for i2 in range(2 * array.shape[1]):
      i = i2 // 2
      for j2 in range(2 * array.shape[0]):
        j = j2 // 2
        if array[j, i] == 0:
          win.addstr("  ")
        elif array[j, i] == 1:
          win.addstr("██")
      newline(win)
      win.refresh()

def main(win, settings: dict, array: NDArray) -> NDArray:
  curses.curs_set(0)
  win.scrollok(True)
  curses.cbreak()
  win.clear()
  gen = 1
  while 1:
    win.addstr(f'Generation: {gen}')
    newline(win)
    drawArray(win, array)
    interval = settings['interval']
    quit = wait(win, interval)
    if quit:
      break
    win.clear()
    array = conway.conwayPass(settings, array)
    gen += 1
    if np.all(array == 0):
      win.clear()
      win.addstr(f"Extinct at generation {gen}\nPress any key to quit to menu...")
      win.refresh()
      win.getch()
      break
  return array
