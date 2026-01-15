import curses
import numpy as np
import config
import cursesui
import seed

def main(win):
  curses.curs_set(0)
  win.scrollok(True)
  curses.cbreak()
  win.clear()
  default_config = config.return_config()['default_config']
  array = seed.main(win, default_config)
  cursesui.main(win, default_config, array)

if __name__ == "__main__":
  curses.wrapper(main)
