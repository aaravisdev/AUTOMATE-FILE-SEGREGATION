import os 
import shutil

from_dir = input("enter directory where the files should be moved from : ")
to_dir = input("enter directory where the filed should be moved to : ")

list_of_files= os.listdir(from_dir)
for file in list_of_files : 
    name,ext = os.path.splitext(file)
    ext = ext [1:]
    if ext == " ":
        continue
if os.path.exists(from_dir + '/' + ext) : 
    shutil.move(from_dir + '/' + file, to_dir + '/' + ext)
else :
    os.makedirs(from_dir+'/'+ext )
    shutil.move(from_dir + '/' + file, to_dir + '/' + ext)
 
print("\033[32m"+ "file moved enjoy :)")