from sys import argv
from os import listdir
from utils import load_config, mover, load_plugins

parsedconfig = {
  "origins": [],
  "file_ext": {},
  "filestarts": {}
}

plugins = {}
args = {}

def main():
  plugins, args = load_plugins()
  load_config()
  

def debug_run():
  return

if __name__ == "__main__":
  main()