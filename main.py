#!/usr/bin/env python3
import curses
import numpy as np
import config
import cursesui
import seed
import setup

def main(win):
  curses.curs_set(0)
  win.scrollok(True)
  curses.cbreak()
  win.clear()
  default_config = config.return_config()['default_config']
  settings, array = setup.main(win, default_config)
  while 1:
    array = seed.main(win, settings, array)
    array = cursesui.main(win, settings, array)

if __name__ == "__main__":
  curses.wrapper(main)
