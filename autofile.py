from sys import argv
from os import listdir
from funcs import load_config, mover


parsedconfig = {
  "origins": [],
  "file_ext": {},
  "filestarts": {}
}

args = {}

def handler():
  return
def run():
  while True:
    mover(parsedconfig)
    
def debug_run():
  return

if __name__ == "__main__":
  handler()