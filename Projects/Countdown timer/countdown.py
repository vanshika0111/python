import time

def CountDown(t):
    while t:
        min, sec = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(min,sec)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("Start working smart.")

t = input("Enter time in seconds: ")
CountDown(int(t))