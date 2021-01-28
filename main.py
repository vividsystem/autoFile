#!bin/env/python3
from json import load
from os import listdir, rename, path, system, getenv
from time import sleep, ctime, strptime, strftime
from json import load
from threading import Thread

config = load(open('/Users/mateostiller/Developer/Code/Projects/Automation/autofile/config.json'))

homedir = getenv('HOME')

parsedconfig = {
  "origins": [],
  "file_ext": {},
  "filestarts": {}
}

def load_config():
  for i in config["origins"]:
    parsedconfig["origins"].append(i)
  for val in config:
    if val == "file_extensions":
      for extension in config["file_extensions"]:
        try:
          for extension_val in config["file_extensions"][extension]:
            for i in config["file_extensions"][extension]["endings"]:
              path = config["file_extensions"][extension]["destination"]
              if path.endswith('/') == False:
                path += '/'
              parsedconfig["file_ext"][i] = [path, config["file_extensions"][extension]["addDate"]] 
        except:
          return
    elif val == "filestarts":
      for start in config["filestarts"]:
        try:

          for startval in config["filestarts"][start]:
            for i in config["filestarts"][start]["starts"]:
              parsedconfig["filestarts"][i] = []
              path = config["filestarts"][start]["directory"]+i
              if path.endswith('/') == False:
                path += '/'
              parsedconfig["filestarts"][i].append(path)
              parsedconfig["filestarts"][i].append(config["filestarts"][start]["addDate"])
        
        except:
          return
  mover()

def ctime_get(filepath):
  creation_time = ctime(path.getctime(filepath))
  conv = strptime(creation_time,"%a %b %d %H:%M:%S %Y")
  formated_time = strftime("%Y-%m-%d_", conv)
  return formated_time


def mover():
  while True:
    for origin in parsedconfig["origins"]:
      for thing in listdir(origin.replace("~", homedir)):
        for i in parsedconfig["file_ext"]:
          path = origin+thing
          if thing.endswith(i):
            addDate = parsedconfig["file_ext"][i][1]
            thingTime = ctime_get(path)

            if addDate == True and thing.startswith(thingTime) == False:
              dest = parsedconfig["file_ext"][i][0].replace('~', homedir) +thingTime +thing
              rename(path, dest)
              #print(dest)

            if addDate == False or thing.startswith(thingTime) == True:
              dest = parsedconfig["file_ext"][i][0].replace('~', homedir)+thing
              rename(path, dest)
              #print(dest)

        for i in parsedconfig["filestarts"]:
          path = origin+thing
          if thing.startswith(i) or thing.startswith(i, 11):
            addDate = parsedconfig["filestarts"][i][1]
            thingTime = ctime_get(path)

            if addDate == True and thing.startswith(thingTime) == False:
              dest = parsedconfig["filestarts"][i][0].replace('~', homedir) +thingTime +thing
              rename(path, dest)
              #print(dest)

            if addDate == False or thing.startswith(thingTime) == True:
              dest = parsedconfig["filestarts"][i][0].replace('~', homedir)+thing
              rename(path, dest)
              #print(dest)

if __name__ == "__main__":
  load_config()
