import os

#Make list
#misc will always be the last element in the list
types = ["hair", "skin_details", "hat", "head_accessory", "body_accessory", "top", "bottom", "full_body", "shoes", "misc"]
subtypes = [["hair"], #hair
            ["overlay", "lash", "blush", "freckle", "mask", "forehead", "mole", "brow"], #skin deet
            ["hat", "beanie"], #hat
            ["glasses", "necklace", "earring", "eyeshadow", "eye", "eyeliner", "blush", "lip", "contacts", "headphone"], #head acc
            ["bracelet", "ring", "sock", "nail", "legging", "glove", "tights", "stocking"], #body acc
            ["top","blouse", "jacket", "hoodie", "shirt", "cardigan", "vest", "tank", "jumper", "sweater", "corset", "blazer", "turtleneck"], #top
            ["pant", "jeans", "shorts", "skirt", "bottom", "cargo", "khaki"], #bottom
            ["dress", "suit"], #full body
            ["boot", "sneaker", "loafer", "shoe"], #shoes 
            ["default", "preset"]] #misc

#Select dir
input_dir = os.path.normpath(input("Select directory: "))
os.chdir(input_dir)

#Make folders
for i in types:
    if os.path.isdir(i):
        pass
    else:
        os.mkdir(i)

#Place files in folders
count = 0
filePathList = []

for root, dirs, files in os.walk(input_dir):
    for f in files:
        b = False
        if os.path.splitext(f)[1] != ".package":
            os.remove(os.path.join(root,f))
            b = True
        for t in types:
            if t in root:
                b = True
        if b == False and os.path.splitext(f)[1] == ".package":
            filePathList.append(os.path.join(root,f))
            


for f in filePathList:
    b = False
    parsed_f = os.path.split(f)[1]
    for subtype in subtypes:
        for folder in subtype:
            if folder in parsed_f.lower() and b == False:
                
                os.rename(f, os.path.join(input_dir, types[subtypes.index(subtype)], parsed_f))
                count += 1
                b = True
                
    if b == False:
        for x in types:
            print(types.index(x), x)
        text = "Input No. for Type of " + f + ": "
        p = int(input(str(text)))
        print(types[p])
        os.rename(f, os.path.join(input_dir, types[p], parsed_f))
        print("moved to "+ os.path.join(input_dir, types[p], parsed_f))

empty = [root for root, dirs, files, in os.walk(input_dir)
                   if not len(dirs) and not len(files)]

for folder in empty:
    os.rmdir(folder)
    print('Removed ', folder, 'as it is now empty')       

print("Moved ", count, "files")

