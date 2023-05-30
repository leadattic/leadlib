import os

def dir(path, type):
  if type == "c" or type == "C":
    os.mkdir(path)
  elif type == "e" or type == "E":
    if os.path.exists(path):
      return True
    else:
      return False
  else:
    return "Type of function does not exist"
   
