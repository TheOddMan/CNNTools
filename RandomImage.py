import random as r
from RandomImageConfig import *
from PIL import Image
from gevent import os
import shutil


ImageNumber = config_ImageNumber  #ImageNumber : If ImageNumber is 51,means to get number 1 to number 50 Image in each classes. Total Image Set
trainingPick = config_trainingPick  #trainingPick : The amount of training images,picks from Total Image Set.  Training Image Set
validationPick = config_validationPick  #validationPcik : The amount of validation images,picks from (Total Image Set - Training Image Set).  Validation Image Set

# Finally, the others Image from (Total Image Set - Training Image Set - Validation Image Set) is testing Image.  Testing Image Set

s = set()
for i in range(1,(ImageNumber+1)):
    s.add(i)
datatraining = r.sample(s,trainingPick)
datatraining = set(datatraining)

remaindata = s - datatraining

datavalidation = r.sample(remaindata,validationPick)
datavalidation = set(datavalidation)

datatest = remaindata-datavalidation
datatest = set(sorted(datatest))

datatraining = sorted(datatraining)
datavalidation = sorted(datavalidation)
datatest = sorted(datatest)



def deletefile(mydir):
    for path, subdirs, files in os.walk(mydir):
     for name in files:
      basedir = os.path.basename(path)
      newpath = path.replace("\\"+basedir,'')
      typeofdatadir = os.path.basename(newpath)
      os.remove(mydir+"\\"+typeofdatadir+"\\"+basedir+"\\"+name)

def splitimage(mydir):
    print("清空資料夾.....")
    deletefile(config_toPath)
    for path, subdirs, files in os.walk(mydir):
        for name in files:
            imagename = name.replace(".jpg","")
            imagenumber = int(imagename.split("_")[1])
            basedir = os.path.basename(path)
            if imagenumber in datatest:
                shutil.copy(path + "\\" + name, "C:\\Users\\409LAB00\\Desktop\\getRandomImageTest\\test\\"+basedir+"\\" + name)
                print("copy "+name+" to testing dataset ")
            elif imagenumber in datatraining:
                shutil.copy(path + "\\" + name, "C:\\Users\\409LAB00\\Desktop\\getRandomImageTest\\train\\"+basedir+"\\" + name)
                print("copy " + name + " to training dataset ")
            elif imagenumber in datavalidation:
                shutil.copy(path + "\\" + name, "C:\\Users\\409LAB00\\Desktop\\getRandomImageTest\\validation\\" +basedir+"\\"+ name)
                print("copy " + name + " to validation dataset ")
    print("training set : ", datatraining)
    print("validation set : ", datavalidation)
    print("test set : ", datatest)

splitimage(config_fromPath)

