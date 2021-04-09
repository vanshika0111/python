#binary search
def Bsearch(AR,ITEM):
     beg=0
     last=len(AR)-1
     while(beg<=last):
          mid=(beg+last)/2
          if(ITEM==AR[mid]):
               return mid
          elif(ITEM>AR[mid]):
               beg=mid+1 
          else:
               last=mid-1
     else:
         return False  #item not found
        


#binary search works only for linear lists


#__main
N= int(input("Enter the size of linear list (max size is 50): "))
print("\n Enter elements for LINEAR LIST in ASCENDING ORDER\n")
AR = [0]*N  #initializes list of size N with zeros

for i in range(N):
     AR[i] = int(input("Element " +str(i)+":"))
     ITEM = int(input("\n Enter element to search: "))
     index = Bsearch(AR,ITEM)

if index:
     print("\nElement found at index: ",index, ", Position: ", (index+1))
else:
     print("\n Ooppss! Element not found.")