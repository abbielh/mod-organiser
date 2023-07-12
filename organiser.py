import os

#Make list
#misc will always be the last element in the list
types = ["hair", "top", "jeans", "shorts", "hoodie", "jacket", "dress", "shoes", "makeup", "misc"]

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
subdir = os.listdir()
filePath = []
for i in subdir:
    if os.path.splitext(i)[1] == ".package":
        filePath.append(i)

for folder in types:
    for file in filePath:
        if file == folder:
            os.rename(input_dir, "\\" + types[folder])
            count += 1
            file.close()
        elif file != folder:
            os.rename(input_dir, "\\" + types[-1])
            count += 1
            file.close()
        else:
            print("file not moved!")

print("Moved ", count, "files")

