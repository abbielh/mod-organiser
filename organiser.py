import os
import shutil
import glob

#Make list
#misc will always be the last element in the list
types = ["hair", "tops", "bottoms", "dresses", "shoes", "makeup", "misc"]

#Select dir
input_dir = input("Select directory: ")
os.chdir(input_dir)

#Make folders
for i in types:
    if os.path.isdir(i):
        pass
    else:
        os.mkdir(i)

def sortDir(list):
    for i in list:
        stringElem = str(i)
        category = "\*" + stringElem + "*"
        pattern = input_dir + category
    return pattern

#Place files in folders
count = 0
fileType = sortDir(types)
for num in types:
    for file in glob.glob(fileType, recursive = False):
        shutil.move(os.path.join(input_dir, file), types[num])
        count += 1
print("Moved ", count, "files")

