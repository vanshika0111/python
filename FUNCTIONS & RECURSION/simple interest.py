#program to find simple interest using function
#def simpleInterest(principal, time=2 , rate=0.10):  #to make time and rate constant
def simpleInterest(principal, time, rate):
    return principal*time*rate

#although time and rate is constant, the argument can still be passed. 

#main
principal = float(input("Enter principal amount: "))
time = int(input("Enter time in years: "))
rate = float(input("Enter rate of interest: "))
interest = simpleInterest(principal, time, rate)
print("Simple interest with the provided data of time ad rate is", interest)
