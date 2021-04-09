#names= {}  #declaring an empty dictionary
#names= []  #declaring an empty list
numberOfPlayer = int( input ("Enter number of players (1<players<15): "))

if(numberOfPlayer <= 15 and numberOfPlayer > 1):
     for i in range (1,numberOfPlayer+1):
          print("Player",i)
          names = input ("Enter name of player: ")
     else:
      print("Enter correct number of players!")

print("TEAM DETAILS")
for i in range(1,numberOfPlayer+1):
    print("Player",i, "is", names)