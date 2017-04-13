import os
import numpy as np
from PIL import Image
#------------------------------------------------------------------------------------------
def get_picname(path):
    return [f for f in os.listdir(path) if f.endswith('.png')or f.endswith('.jpg')]
#------------------------------------------------------------------------------------------
std_img = Image.open('./standard.png')
backgroundThreshold = 100
std_img_arr = np.array(std_img)
std_img_arr[std_img_arr>backgroundThreshold]=255
std_shape = std_img_arr.shape[1::-1]
#------------------------------------------------------------------------------------------
EMUN_rotation = [Image.ROTATE_90,Image.ROTATE_180,Image.ROTATE_270]
path = "pictures"
for picname in get_picname(path):
    imgdir = os.path.join(path,picname)
    img = Image.open( imgdir)
    #initial
    best_rat = 1
    best_img        = img.resize(std_shape)
    img_resize_arr  = np.array(best_img)
    img_resize_arr[img_resize_arr>backgroundThreshold]=255
    min_diffValue   = np.abs(img_resize_arr-std_img_arr).mean()
    for rotation_rat in EMUN_rotation:        
        #rotate the image
        img_rotated     = img.transpose(rotation_rat)
        img_resize      = img_rotated.resize(std_shape)
        img_resize_arr  = np.array(img_resize)
        img_resize_arr[img_resize_arr>backgroundThreshold]=255
        diffValue       = np.abs(img_resize_arr-std_img_arr).mean()
        if diffValue<min_diffValue:
            min_diffValue = diffValue
            best_img      = img_resize
    best_img.save(os.path.join("clean_pictures",picname))

