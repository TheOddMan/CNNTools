from MakeDirs_config import *
import os



def MakeDirs(pathxxx): #在指定資料夾內建立資料夾
    for num in range(1,(config_DirAmount+1)):
        os.makedirs(pathxxx+"\\B"+str(num))
        print(pathxxx+"\\B"+str(num))

MakeDirs(config_path)