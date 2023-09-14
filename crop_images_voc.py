import glob
import os
import pickle
import xml.etree.ElementTree as ET
from os import listdir, getcwd
from os.path import join
# dirs = '/Users/rx/NTU/MDP/MDP-CV.v6i.voc/train/'
from PIL import Image
dict2 = {'11': '0', '12': '1', '13': '2', '14': '3', '15': '4', '16': '5', '17': '6', '18': '7', '19': '8', '20': '9', '21': '10', '22': '11', '23': '12', '24': '13', '25': '14', '26': '15', '27': '16', '28': '17', '29': '18', '30': '19', '31': '20', '32': '21', '33': '22', '34': '23', '35': '24', '36': '25', '37': '26', '38': '27', '39': '28', '40': '29', 'wa': '30'}

# Print each item on a new line

def convert_annotation():
    # basename = os.path.basename(image_path)
    # print(image_path)
    # basename_no_ext = os.path.splitext(basename)[0]

    # in_file = open(dir_path + '/' + basename_no_ext + '.xml')
    dirs = '/Users/rx/NTU/MDP/MDP-CV.v6i.voc/tempp/train/'
    count=2800
    for images in os.listdir(dirs):
        count+=1
        in_file = dirs + images
        # print(in_file)
        if images.endswith(".xml"):
            tree = ET.parse(in_file)
            root = tree.getroot()
            size = root.find('size')
            w = int(size.find('width').text)
            h = int(size.find('height').text)

            for obj in root.iter('object'):
                difficult = obj.find('difficult').text
                cls = obj.find('name').text
                xmlbox = obj.find('bndbox')

                b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
                # print(b)

                if (cls == "38"):
                    print("try"+str(count))
                    
                    temp = in_file.replace("xml","jpg")
                    im = Image.open(temp)
            

                
                # Cropped image of above dimension
                # (It will not change original image)
                    im1 = im.crop((b[0], b[2], b[1], b[3]))
                    
                    # Shows the image in image viewer
                    # im1.show()
                    save_path = "/Users/rx/NTU/MDP/MDP-CV.v6i.voc/dest/"
                    if not os.path.exists(save_path):
            
                        os.mkdir(save_path) 
                    
                    im1.save(save_path+"/"+str(count)+"_"+dict2[cls]+'.jpg')
            
convert_annotation()