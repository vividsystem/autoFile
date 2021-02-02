from yaml import load, FullLoader
from time import ctime, strptime, strftime
from os import listdir, rename, getenv, path
homedir = getenv("HOME")

def ctime_get(filepath):
  creation_time = ctime(path.getctime(filepath))
  conv = strptime(creation_time,"%a %b %d %H:%M:%S %Y")
  formated_time = strftime("%Y-%m-%d_", conv)
  return formated_time

def load_config(parsedconfig, *args, **kwargs):

  #loads the yaml config file
  config = load(open(homedir+'/.config/autofile/config.yaml'), Loader=FullLoader)

  # getting the places where it looks for files
  for i in config["origins"]:
    parsedconfig["origins"].append(i)


  #converting the file extensions that should be sorted in an easier to use model
  if "file_extensions" in config and  "filestarts" in config:
    for extension in config["file_extensions"]:

      try:
        for extension_val in config["file_extensions"][extension]:
          for i in config["file_extensions"][extension]["endings"]:

            # making path var for ease of use
            path = config["file_extensions"][extension]["destination"]
            if path.endswith('/') == False:
              path += '/'

            #append the easier model of the config
            parsedconfig["file_ext"][i] = []
            parsedconfig["file_ext"][i].append(path)
            parsedconfig["file_ext"][i].append(config["file_extensions"][extension]["addDate"])
      except:
        return
    #basically same as with file extensions
    for start in config["filestarts"]:

      try:
        for startval in config["filestarts"][start]:
          for i in config["filestarts"][start]["starts"]:
            
            #making path var for ease of use
            path = config["filestarts"][start]["directory"]+i
            if path.endswith('/') == False:
              path += '/'

            #append the easier model of the config
            parsedconfig["filestarts"][i] = []
            parsedconfig["filestarts"][i].append(path)
            parsedconfig["filestarts"][i].append(config["filestarts"][start]["addDate"])
      except:
        return

def mover(parsedconfig):
    #looping trough the directory where the code is supposed to look after files
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