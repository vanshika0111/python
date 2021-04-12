#get the number of secomds from the user
numSeconds = int(input("Enter number of seconds: "))

#extract the number of minutes using integer division
numMinutes = numSeconds//60

#extract the number of seconds remaining since the last minute usinf the modulo
remainingSeconds = numSeconds % 60

print("miutes: ",numMinutes)
print("seconds: ",remainingSeconds)
