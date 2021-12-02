import os
import shutil
path = "/Users/Navneet/Desktop/Class99"
print("before moving the file")
print(os.listdir(path))
source = "/Users/Navneet/Desktop/Class99/newFile.txt"
destination = "/Users/Navneet/Desktop/Class99/myFolder"
dest = shutil.move(source,destination)
print("after moving the file")
print(os.listdir(path))