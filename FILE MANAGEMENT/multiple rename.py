#myfile = open("image","a")
#for line in myfile:
#    print(line)
#myfile.close()

#import os
#os.rename(r'C:\Users\HP WORLD\Desktop\mbit clg\vs\weather',r'C:\Users\HP WORLD\Desktop\mbit clg\vs\app')


import os
os.chdir(r'C:\Users\HP WORLD\Desktop\mbit clg\vs\trial img')  #paste your file location
i=1
for file in os.listdir():
    src=file
    dst=str(i)+".jpg"
    os.rename(src,dst)
    i+=1