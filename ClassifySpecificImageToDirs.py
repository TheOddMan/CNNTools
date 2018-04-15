import os,shutil
from ClassifySpecificImageToDirs_config import  *
from DeleteAllFileFromDirs import  *
moveto=config_toPath #ClassifySpecificImage function 使用之路徑


def ClassifySpecificImage(mydir): #從指定資料夾內所有圖片(包含子資料夾)分類出指定檔名圖片至指定資料夾
 deletefile(moveto)
 for path, subdirs, files in os.walk(mydir):

  basename = ''
  for name in files:
    basename = name.split('_')[0]
    shutil.copy(path+"\\"+name,moveto+"\\"+basename+"\\"+name)


ClassifySpecificImage(config_fromPath)