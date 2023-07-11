import os
import shutil
import glob

#Make list
#misc will always be the last element in the list
types = ["hair", "facial accessories", "tops", "bottoms", "dresses", "shoes", "makeup", "misc"]

#Select dir
input_dir = input("Select directory: ")
os.chdir(input_dir)

#Make folders
for i in types:
    if os.path.isdir(i):
        pass
    else:
        os.mkdir(i)

#Place files in folders
count = 0
pattern = input_dir + "\*hair*"
for file in glob.glob(pattern, recursive = False):
    shutil.move(os.path.join(input_dir, file), types[0]) 