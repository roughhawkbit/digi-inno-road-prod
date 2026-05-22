import os


def find_highest_numbered_subdir(directory):
  subdirs = os.listdir(directory)
  num = 0
  highest = None
  for subdir in subdirs:
    s_num = int(subdir.split('-')[-1])
    if s_num > num:
      num = s_num
      highest = subdir
  return highest


def secrets_path():
  p = os.path.abspath(__file__)
  p = os.path.join(p, "../../secrets")
  p = os.path.abspath(p)
  return p
