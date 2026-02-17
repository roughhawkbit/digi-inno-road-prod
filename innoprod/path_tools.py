import os.path

def secrets_path():
  p = os.path.abspath(__file__)
  p = os.path.join(p, "../../secrets")
  p = os.path.abspath(p)
  return p