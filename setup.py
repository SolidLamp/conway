import curses
import time
from typing import Tuple
import numpy as np
from numpy._typing import NDArray
import tui

__maxinterval__ = 10
__maxwidth__ = 80
__maxheight__ = 20
__min__ = 0
__intervalstep__ = 0.05

def init(win: curses.window) -> None:
  string = ''
  for i in range(20):
    string = string + 'd\n'
  tui.print3(win, string, 0, 0, 0)
  win.refresh()
  time.sleep(0.3)
  win.clear()

def drawBorder(win: curses.window) -> None:
  pass

def delta(win: curses.window, var: int | float, min: int | float, max: int | float, varName: str, step: float | int = 1) -> int | float:
  vardelta = 0
  while vardelta != 2:
    vardelta = tui.option(win, f"{varName}: {var}", [f'+{step}', f'-{step}', 'Done'])
    match vardelta:
      case 0:
        var += step
      case 1:
        var -= step
    if var > max:
      var = max
    if var < min:
      var = min
  return(var)

def main(win: curses.window, settings: dict) -> Tuple[dict, NDArray]:
  init(win)
  wrap = tui.option(win, "Enable grid wrapping?", ['Yes', 'No'])
  settings['wrap'] = not(bool(wrap))
  interval = delta(win, settings['interval'], __min__, __maxinterval__, 'Interval', __intervalstep__)
  settings['interval'] = interval
  h = delta(win, settings['width'], __min__, __maxheight__, 'Height')
  settings['height'] = h
  w = delta(win, settings['width'], __min__, __maxwidth__, 'Width')
  settings['width'] = w
  array = np.zeros((w, h))
  return(settings, array)

