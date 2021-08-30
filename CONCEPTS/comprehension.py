# comprehension

# ----------- LIST COMPREHENSION---------------
# METHOD 1
list = []
for i in range (100):
    if i%3 == 0:
        list.append(i)
      
print(list)

# METHOD 2
list2 = [i for i in range(100) if i%3==0]
print(list2)

# ----------- DICTIONARY COMPREHENSION---------------
# METHOD 1
dict = { 0:"item 0", 1:"item 1"}
print(dict)

# METHOD 2
dict1 = { i:f"item {i}" for i in range(5) if i%2==0}
print(dict1)
dict1 = { value:key for key, value in dict1.items()}
print(dict1)

# ----------- SET COMPREHENSION---------------
dress = { dress for dress in ["dress1", "dress2", "dress3", "dress3", "dress1", "dress2", "dress4"]}
print(dress)
print(type(dress))

# ----------- GENERATOR COMPREHENSION---------------
even = (i for i in range(10) if i%2==0)
print(even)
print(type(even))
# METHOD 1
print(even.__next__())
print(even.__next__())
# METHOD 2
for item in even:
    print(item)