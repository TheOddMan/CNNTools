import os
from DeleteAllFileFromDirs_config import *

def deletefile(mydir):
    for path, subdirs, files in os.walk(mydir):
     for name in files:
      os.remove(path+"\\"+name)

deletefile(config_path)