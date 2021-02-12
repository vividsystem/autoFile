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
repo_dir = getcwd()+'/'+__file__ if __file__.startswith(homedir) == False else __file__
def main():
  load_config(parsedconfig)
  while True:
    mover(parsedconfig)

def debug_run():
  return

#if __name__ == "__main__":
  #main()
