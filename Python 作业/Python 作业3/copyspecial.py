#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dirname):
  """返回给定目录中特殊文件的绝对路径的列表"""
  result = []
  paths = os.listdir(dirname) # 该目录的路径列表
  for fname in paths:
    match = re.search(r'__(\w+)__',fname)
    if match:
      result.append(os.path.abspath(os.path.join(dirname,fname)))
  return result


def copy_to(paths,to_dir):
  """ 将所有给定的文件复制到给定的目录，必要时创建它。"""
  if not os.path.exists(to_dir):
    os.mkdir(to_dir)
  for path in paths:
    fname = os.path.basename(path)
    shutil.copy(path, os.path.join(to_dir, fname))
    # 如果os.path.exists()存在，则可能出错

def zip_to(paths,zipfile):
  """将所有给定文件压缩成具有给定名称的新Zip文件。"""
  cmd = '7z a ' + zipfile + ' ' + ' '.join(paths)
  print("Command I'm going to do:" + cmd)
  (status, outout) = subprocess.getstatusoutput(cmd)
  if status:
    sys.stderr.write(outout)
    sys.exit(1)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print("usage: [--todir dir][--tozip zipfile] dir [dir ...]");
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print("error: must specify one or more dirs")
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  paths = []
  for dirname in args:
    paths.extend(get_special_paths(dirname))

    if todir:
      copy_to(paths, todir)
    elif tozip:
      zip_to(paths ,tozip)
    else:
      print('\n'.join(paths))

if __name__ == "__main__":
  main()
