
import matplotlib.pyplot as plt
from keras.preprocessing import image
import os
import glob
from DeleteAllFileFromDirs import *
import numpy as np
from ImageGenerator_config import *
import uuid
path=config_fromPath


from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

datagen_rotation = ImageDataGenerator(rotation_range=360,fill_mode='constant')
datagen_shift = image.ImageDataGenerator(width_shift_range=10,height_shift_range=10,fill_mode='constant')
datagen_zoom_out = image.ImageDataGenerator(zoom_range=[1,1.5],fill_mode='constant')
datagen_zoom_in = image.ImageDataGenerator(zoom_range=[0.5,1],fill_mode='constant')


def generator(img,new_path,basename):
    new_path = config_toPath
    x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
    x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

    gen_data_rotation = datagen_rotation.flow(x, batch_size=1,save_to_dir=new_path+"\\"+basename, save_prefix='', save_format='jpeg')
    gen_data_shift =datagen_shift.flow(x, batch_size=1,save_to_dir=new_path+"\\"+basename, save_prefix='', save_format='jpeg')
    gen_data_zoom_out = datagen_zoom_out.flow(x, batch_size=1,save_to_dir=new_path+"\\"+basename, save_prefix='', save_format='jpeg')
    gen_data_zoom_in = datagen_zoom_in.flow(x, batch_size=1,save_to_dir=new_path+"\\"+basename, save_prefix='', save_format='jpeg')

    if(config_rotation.lower() == 'on'):
     for i in range(config_rotation_amount):
         gen_data_rotation.next()
    if(config_shift.lower() == 'on'):
     for i in range(config_shift_amount):
         gen_data_shift.next()
    if(config_zoom_out.lower() == 'on'):
     for i in range(config_zoom_out_amount):
         gen_data_zoom_out.next()
    if(config_zoom_in.lower() == 'on'):
     for i in range(config_zoom_in_amount):
         gen_data_zoom_in.next()



deletefile(config_toPath)

for path, subdirs, files in os.walk(path):
     for name in files:
# # name = 檔名.jpg     path指到最接近檔案的資料夾
      print("Load Image : " + name)
      img = load_img(path + "\\"+name)
      print("Generate Image from " + name + "...")
      print("path : ",path)
      print("basename : ", os.path.basename(path))


      generator(img,path,os.path.basename(path))

for pathz, subdirs, files in os.walk(config_toPath):
    count = 1
    bbbbasename = os.path.basename(pathz)
    for name in files:
     sssbasename = os.path.basename(pathz)
     trainOrvalidation = os.path.basename(pathz.replace('\\'+sssbasename,''))
     print("sssbasename : "+sssbasename)
     print(os.path.basename(pathz.replace('\\'+sssbasename,'')))
     if(name != sssbasename+'_'+str(count)+'.jpg'):
      print('Change Name : ' +name+" to Name : " + sssbasename + '_' + str(count) + '.jpg' )
      os.rename(pathz + "\\" + name, pathz + "\\" + sssbasename + '_' + str(count)  + '.jpg')

     count+=1

for pathz, subdirs, files in os.walk(config_toPath):
    count = 0
    basename = os.path.basename(pathz)
    for name in files:
     count+=1
    print("Dir " + basename +" have "+ str(count) + " images.")
