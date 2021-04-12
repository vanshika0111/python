list = [15,6,78,34,90]
print("Before sorting: ",list)
n = len(list)
for i in range(1,n):
    key = list[i]
    j = i-1
    while j>=0 and key<list[j]:
        list[j+1] = list[j]
        j = j-1
    else:
        list[j+1] = key
         

print("After sorting: ",list)