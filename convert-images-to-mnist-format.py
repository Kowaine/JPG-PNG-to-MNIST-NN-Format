import os
from PIL import Image
from array import *
from random import shuffle
import numpy as np

# Load from and save to
Names = [['training-images','train'], ['t10k-images','t10k']]

for name in Names:
    
    data_image = array('B')
    #data_image = []
    data_label = array('B')

    FileList = []
    for dirname in os.listdir(name[0]):
        path = os.path.join(name[0],dirname)
        for filename in os.listdir(path):
            if filename.endswith(".png"):
                FileList.append(os.path.join(name[0],dirname,filename))

    shuffle(FileList) # Usefull for further segmenting the validation set

    if len(FileList) == 0:
        continue

    for filename in FileList:

        label = int(filename.split('\\')[1])

        Im = Image.open(filename).convert("L")

        pixel = Im.load()

        width, height = Im.size

        for x in range(0,width):
            for y in range(0,height):
                data_image.append(pixel[y, x])

        data_label.append(label) # labels start (one unsigned byte each)

    hexval = "{0:#0{1}x}".format(len(FileList),6) # number of files in HEX

    # header for label array

    header = array('B')
    header.extend([0,0,8,1,0,0])
    header.append(int('0x'+hexval[2:][:2],16))
    header.append(int('0x'+hexval[2:][2:],16))
    
    data_label = header + data_label

    # additional header for images array
    
    if max([width,height]) <= 256:
        header.extend([0,0,0,width,0,0,0,height])
    else:
        raise ValueError('Image exceeds maximum size: 256x256 pixels');

    header[3] = 3 # Changing MSB for image data (0x00000803)
    
    data_image = header + data_image

    output_file = open(name[1]+'-images-idx3-ubyte', 'wb')
    data_image.tofile(output_file)
    output_file.close()

    output_file = open(name[1]+'-labels-idx1-ubyte', 'wb')
    data_label.tofile(output_file)
    output_file.close()

# gzip resulting files

for name in Names:
    # 根据自己安装的压缩软件修改
    os.system('7z a -tgzip '+name[1]+'-images-idx3-ubyte.gz '+name[1]+'-images-idx3-ubyte')
    os.system('7z a -tgzip '+name[1]+'-labels-idx1-ubyte.gz '+name[1]+'-labels-idx1-ubyte')
