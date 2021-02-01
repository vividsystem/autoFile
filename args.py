from sys import argv

class ArgParser:
  def __init__(self,args, description="", prog="", prefix="-"):
    self.description = description
    self.prog = prog
    self.args = args
    self.prefix = prefix

  def parse_args(self):
    args = {}
    for num in range(len(self.args)):
      if self.args[num].startswith(self.prefix):
        argname = self.args[num].strip(self.prefix[0])
        if self.args[num+1].startswith(self.prefix) == False:
          args[argname] = self.args[num+1]
    return args