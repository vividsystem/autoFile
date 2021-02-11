from sys import argv
from os import listdir, getenv


get_plugins = lambda : listdir(getenv("HOME")+"/.config/autofile/plugins")
print(get_plugins())