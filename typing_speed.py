from time import *
import random as r 
def mistake (partest,usertest):
    error = 0
    for i in range (len(partest)):
        try:
            if partest[i]!= usertest[i]:
                error = error + 1 
        except:
            error = error +1
    return error
def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(userinput)/time_R
    return round(speed)

test = ["this is my own program","to practice and learn typing","and to calculate the speed"]
test1 = r.choice(test)
print("********typing speed *********")
print(test1)
print()
print()
time_1 = time()
testinput = input("Enter :")
time_2 = time()
print("Speed :", speed_time(time_1,time_2,testinput),"w/s")
print("Error :",mistake(test1,testinput))