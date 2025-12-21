import curses
import time
import os
import numpy as np
from numpy._typing import NDArray
import cursesui

def displayCursor(win, array: NDArray, posy: int, posx: int):
  curses.start_color()
  curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
  win.move(posy * 2 + 4, posx * 4)
  if array[posx, posy] == 1:
    win.addstr('####', curses.color_pair(1))
  else:
    win.addstr('####', curses.A_NORMAL)
  win.move(posy * 2 + 5, posx * 4)
  if array[posx, posy] == 1:
    win.addstr('####', curses.color_pair(1))
  else:
    win.addstr('####', curses.A_NORMAL)
  win.addstr('', curses.A_NORMAL)
  win.refresh()

def main(win):
  curses.curs_set(0)
  win.scrollok(True)
  curses.cbreak()
  win.clear()
  time.sleep(1)
  userinput = 1
  array = np.zeros((10, 10))
  posx = 0
  posy = 0
  while userinput:
    win.addstr('0 - Disable pixel | 1 - Enable pixel | RETURN - Run simulation'
               '\nR - Randomise board | C - Clear board | F - Fill board'
               '\nUP - Move up | DOWN - Move down |'
               ' RIGHT - Move right | LEFT - Move left')
    coords = f'({posx},{posy})'
    #win.addstr(coords)
    cursesui.newline(win)
    cursesui.newline(win)
    cursesui.drawArray(win, array)
    displayCursor(win, array, posy, posx)
    win.refresh()
    try:
      key = win.getkey()
    except Exception:
      key = 'KEY_UP'
    match key:
      case 'KEY_UP':
        posy -= 1
        if posy < 0:
          posy = 0
      case 'KEY_DOWN':
        posy += 1
        if posy > 9:
          posy = 9
      case 'KEY_RIGHT':
        posx += 1
        if posx > 9:
          posx = 9
      case 'KEY_LEFT':
        posx -= 1
        if posx < 0:
          posx = 0
      case '0':
        array[posx, posy] = 0
      case '1':
        array[posx, posy] = 1
      case os.linesep:
        userinput = 0
      case 'c':
        array = np.zeros((10,10))
      case 'f':
        array = np.ones((10,10))
      case 'r':
        array = np.random.randint(0, 2, size=(10, 10))
    win.clear()
  return arrays
