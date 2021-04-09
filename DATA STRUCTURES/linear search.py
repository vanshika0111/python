#linear search

def Lsearch(AR,ITEM):
   i=0
   while i< len(AR) and AR[i] != ITEM:
      i += 1 
   if i < len(AR):
      return i 
   else:
      return False



#main

N = int(input("Enter the desired linear list size (max size is 50): "))
print("\n Enter elements for linear list:\n")
AR = [0]*N   #initializes list of size N with zeros

for i in range(N):
     AR[i] = int(input("Element " + str(i) +":"))
     ITEM = int(input("\n Enter element to search:"))
     index = Lsearch(AR,ITEM)

if index:
     print("\n Element found at index: ",index, ",Position: ",(index+1))
else:
     print("\n Ooppss! Element not found.")