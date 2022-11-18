from PIL import Image
import glob
import os

#?to convert JPEG format images to JPG format for easy training
#edit directory to folder where the images are located
directory = ''
OG_format = 'JPEG'

def img2jpg(directory,OG_format):
    for filename in os.listdir(directory):
        # print(filename)
        if filename.endswith(OG_format):
            im = Image.open(directory + '/' + filename)
            filename = filename.replace(OG_format, "jpg")
            # print(directory + '/' + filename)
            im.save(directory + '/' + filename)

#delete the original JPEG files
def delete_files(directory,OG_format):
    for filename in os.listdir(directory):
        if filename.endswith(OG_format):
            image_path = directory + '/' + filename
            os.remove(image_path)

def main():
    img2jpg(directory,OG_format)
    # delete_files(directory=directory, OG_format= OG_format)

if __name__ == "__main__":
    main()