#to edit the paths of images in txt file


file1 = open('/home/yusuff/Desktop/Panasonic/test/coco/labels.list', 'r')
file2 = open('/home/yusuff/Desktop/Panasonic/test/coco/labels2.txt', 'w')
Lines = file1.readlines()
for line in Lines:
    line = 'data/merge_folder/' + line
    file2.writelines(line)