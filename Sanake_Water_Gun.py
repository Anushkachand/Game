import random

def check(comp, user ): # comp= computer
    if comp == user:
        return 0
    # Sanke(0) drink water(1) - win sanke  
    if ( comp ==0 and user ==1):
        return -1
    elif (comp == 0 and user == 2):
        return 1
    elif (comp == 1 and user == 0):
        return -1
    elif (comp == 1 and user == 2):
        return - 1   
    elif (comp == 2 and user == 0 ):
        return -1
    elif (comp ==2 and user == 1):
        return 1
    

comp = random.randint(0,2)
user = int(input(" 0 for Sanke , 1 for Water and 2 for Gun:\n "))

score = check (user ,comp)
print( f" Computer chose{comp} , You chose {user} ")
if (score ==0):
    print("Its draw")
elif ( score == -1):
    print(" Yoy are lost /n Best of Luck Try next time")
else:
    print(" You are  Winner")
