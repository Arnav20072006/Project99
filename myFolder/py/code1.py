import os
import shutil
path = "/Users/Navneet/Desktop/Class99"
print("before copying the file")
print(os.listdir(path))
source = "/Users/Navneet/Desktop/Class99/newFile.txt"
destination = "/Users/Navneet/Desktop/Class99/newFile2.txt"
dest = shutil.copy(source,destination)
print("after copying the file")
print(os.listdir(path))