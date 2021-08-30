import json

# ----------JSON.LOADS----------
data = '{"var1":"hi", "var2":"bye"}'
print(data)
# print(data['var1'])  --> throws an error
parsed = json.loads(data)
print(parsed)
# print(data['var1'])
""""
used for deserializing native string, byte, or byte array 
which consists of JSON data into Python Dictionary
"""

# ----------JSON.DUMPS----------
data2 = {"var3":"hello", "var4":["see yaa", "night"], "var5":("sun","moon","stars"), "evening":False}
jscompare = json.dumps(data2)
print(jscompare)
"""
in data2, last va;ue "False" has F capital in python
Json is originally of js
in js, "False" has a lowercase f
thus, json.dumps converts data2 into js friendly manner
"""

# ---------DEFINITIONS-------
"""
json.load(): - takes a file object and returns the json object
             - used to read JSON encoded data from a file and convert it 
               into a Python dictionary and deserialize a
               file itself i.e. it accepts a file object.

json.loads() - method can be used to parse a valid JSON string
               and convert it into a Python Dictionary
             - used for deserializing native string, byte, or byte array
               which consists of JSON data into Python Dictionary
"""
