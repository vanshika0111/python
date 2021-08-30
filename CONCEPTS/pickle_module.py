# pickle module (built-in module)

import pickle

# pickling a python object
object = ["sun", "moon", "star", "satellite"]
file = "MyObj.pkl"
fileobject = open(file, "wb")
pickle.dump(object, fileobject)
# dump takes file object as an argument & not a file
fileobject.close()

# de-pickling a python object
file = "MyObj.pkl"
fileobject = open(file, "rb")
MyObj = pickle.load(fileobject)
print(MyObj)
print(type(MyObj))

# difference between pickle.load & pickle.loads