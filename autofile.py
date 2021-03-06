#!/usr/bin/env python3
from sys import argv
from os import listdir, getenv, getcwd, system
from utils import load_config, mover, load_specific_plugin
parsedconfig = {
  "origins": [],
  "file_ext": {},
  "filestarts": {}
}
plugins = {}
args = {}
homedir = getenv("HOME")

repo_dir = getcwd()+'/'+__file__.strip("autofile.py") if __file__.startswith(homedir) == False else __file__.strip("autofile.py")
def main():
  for index_number in range(len(argv)):
    if argv[index_number] == "-p" or argv[index_number] == "--plugin":
      if index_number+1 <= len(argv)-1:
        plugin_name = argv[index_number+1]
        print(repo_dir+"plugins/")
        plugin = load_specific_plugin(plugin_name,repo_dir+"plugins/")
        plugin.main()
      else:
        raise ValueError("No Value specified for -m")
  if "update" in argv:
    system("git pull")
      
    
def debug_run():
  return

if __name__ == "__main__":
  main()
