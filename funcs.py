def plugin(func):
  def wrapper():
    func()
  return wrapper

def load_plugin(name):
  mod = __import__("plugins/%s" % name)
  return mod,

def call_plugin(name, *args, **kwargs):
  plugin = load_plugin(name)
  plugin.plugin_main(*args, **kwargs)