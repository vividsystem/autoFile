from yaml import load, FullLoader
from os import getenv, system, path

def main():
  homedir = getenv("HOME")
  config = load(open(homedir+'/.config/autofile/config.yaml'), Loader=FullLoader)
  for group in config["plugins"]["backup"]:
    for file_to_backup in config["plugins"]["backup"][group]["files"]:
      file_to_backup = file_to_backup.replace('~', homedir)
      dest = config["plugins"]["backup"][group]["backup_directory"].replace('~', homedir)
      if path.exists(dest) != False:
        system("mkdir -p "+dest)
      system("cp -R "+file_to_backup+" "+dest)