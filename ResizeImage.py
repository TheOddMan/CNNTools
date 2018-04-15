import os
from PIL import Image
from ResizeImage_config import *
def im_resize(mydir):
    for path, subdirs, files in os.walk(mydir):
     for name in files:

        image  = Image.open(path+"\\"+name)
        image= image.resize((config_Image_Size,config_Image_Size), Image.ANTIALIAS)
        print("Resize Image "+name+"to "+str(config_Image_Size)+"x"+str(config_Image_Size))
        image.save(path+"\\"+name)

im_resize(config_fromPath)