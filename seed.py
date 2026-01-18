import curses
import time
import os
import sys
import numpy as np
from numpy._typing import NDArray
import config
import cursesui

__maxsmall__ = 10

def displayCursor(win, array: NDArray, posy: int, posx: int):
  curses.start_color()
  curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
  large = array.shape[0] > __maxsmall__ or array.shape[1] > __maxsmall__
  if large:
    cursorstr = '#'
    win.move(posy + 4, posx)
  else:
    cursorstr = '####'
    win.move(posy * 2 + 4, posx * 4)
  if array[posx, posy] == 1:
    win.addstr(cursorstr, curses.color_pair(1))
  else:
    win.addstr(cursorstr, curses.A_NORMAL)
  if not(large):
    win.move(posy * 2 + 5, posx * 4)
  if array[posx, posy] == 1 and not(large):
    win.addstr(cursorstr, curses.color_pair(1))
  elif not(large):
    win.addstr(cursorstr, curses.A_NORMAL)
  win.addstr('', curses.A_NORMAL)
  win.refresh()

def main(win, settings: dict, array: NDArray) -> NDArray:
  win.clear()
  h = settings['height']
  w = settings['width']
  keybinds = config.return_config()['keybinds']
  time.sleep(1)
  userinput = 1
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
      key = keybinds['Move_Up']
    match key:
      case 'KEY_UP':
        posy -= 1
        if posy < 0:
          posy = 0
      case 'KEY_DOWN':
        posy += 1
        if posy > (h - 1):
          posy = (h - 1)
      case 'KEY_RIGHT':
        posx += 1
        if posx > (w - 1):
          posx = (w - 1)
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
        array = np.zeros((w, h))
      case 'f':
        array = np.ones((w, h))
      case 'r':
        array = np.random.randint(0, 2, size=(w, h))
      case 'q':
        sys.exit()
    win.clear()
  return array
