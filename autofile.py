from sys import argv
from os import listdir
from funcs import load_config, mover, load_plugins

parsedconfig = {
  "origins": [],
  "file_ext": {},
  "filestarts": {}
}

args = {}

def main():
  load_plugins()
  #load_config(parsedconfig)
  #run()
def run():
  while True:
    mover(parsedconfig)
    
def debug_run():
  return

if __name__ == "__main__":
  main()