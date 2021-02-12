#!/usr/bin/env python3
from sys import argv
from os import listdir, getenv, getcwd
from utils import load_config, mover, load_plugins
parsedconfig = {
  "origins": [],
  "file_ext": {},
  "filestarts": {}
}

plugins = {}
args = {}
homedir = getenv("HOME")
#repo_dir = getenv("HOME")+"/"+
repo_dir = getcwd()+'/'+__file__.strip("autofile.py") if __file__.startswith(homedir) == False else __file__.strip("autofile.py")
def main():
  for index_number in range(len(argv)):
    if argv[index_number] == "-m":
      if index_number+1 <= len(argv)-1:
        module = argv[index_number+1]+".py"
        if module in listdir(repo_dir+"plugins/") and module != "__init__.py" and module != "__pycache__":
          print("Module found!")
      else:
        raise Exception("No Value specified for -r")
def debug_run():
  return

if __name__ == "__main__":
  main()
