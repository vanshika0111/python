# program to format all the file's names of a directory

import os

def change(path,file,format):
    os.chdir(path)
    i=1
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")

    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())
        if os.path.splitext(file)[1] == format:
            os.rename(file, f"{i}{format}")
            i +=1

change(r"E:\VANSHIKA\photos\& its pics!!", r"E:\VANSHIKA\mbit clg\vs\output\dir_format", ".png")

