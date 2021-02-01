from sys import argv
from os import listdir
from funcs import load_config, mover
from args import ArgParser

parsedconfig = {
  "origins": [],
  "file_ext": {},
  "filestarts": {}
}

args = {}

def handler():
  parser = ArgParser(argv, description='Managing your files like a god.', prog="File managment programm", prefix="-")
  args = parser.parse_args()
  load_config(parsedconfig)
  run()

def run():
  while True:
    mover(parsedconfig)
    
def debug_run():
  return

if __name__ == "__main__":
  handler()