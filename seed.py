import curses
import math
import time
import numpy as np
from numpy._typing import NDArray
import conway
import cursesui

def displayCursor(win, array: NDArray, posx: int, posy: int):
  #win.move(2 * posx, 2 * posy)
  curses.start_color()
  curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
  win.move(4, 8)
  cursesui.newline(win, 2)
  if array[posy, posx] == 1:
    win.addstr('####', curses.color_pair(1))
  else:
    win.addstr('####', curses.A_NORMAL)
  #win.move(2 * posx + 1, 2 * posy)
  cursesui.newline(win)
  if array[posy, posx] == 1:
    win.addstr('####', curses.color_pair(1))
  else:
    win.addstr('####', curses.A_NORMAL)
  win.addstr('', curses.A_NORMAL)
  win.refresh()

def main(win):
  curses.curs_set(0)
  win.scrollok(True)
  curses.cbreak()
  win.addstr("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
  win.clear()
  time.sleep(1)
  userinput = 1
  #array = np.zeros((10, 10))
  array = np.random.randint(0, 2, size=(10, 10))
  while userinput:
    posx = 0
    posy = 0
    win.addstr('0 - Disable pixel | 1 - Enable pixel | RETURN - Run simulation'
               '\nUP - Move up | DOWN - Move down |'
               ' RIGHT - Move right | LEFT - Move left')
    cursesui.newline(win)
    cursesui.newline(win)
    cursesui.drawArray(win, array)
    displayCursor(win, array, 8, 8)
    win.getch()
    try:
      key = win.getkey()
    except Exception:
      key = 'KEY_UP'
    match key:
      case 'KEY_UP':
        pass
    win.clear()
  return array
