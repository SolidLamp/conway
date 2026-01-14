import os
import tomllib

default_config = {
  "interval": 0.5,
  "wrap": False,
}

def return_config():
  if not os.path.exists('config.toml'):
      return default_config
  else:
      with open("config.toml", "rb") as f:
          config = tomllib.load(f).copy()
      return config#['config']
