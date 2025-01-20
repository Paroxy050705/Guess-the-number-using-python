import random

target=random.randint(1,100)
print(target)

while True:
    #take nmber from user
    usernum=input("Guess the number or Quit(Q):")

    #if user want to quit
    if(usernum=="Q"):
        break

    #convert usernum to int for compare with target value
    usernum=int(usernum)
    if(usernum==target):
        print("Congratulation!!!You guess correct..")
        break
    elif(usernum<target):
        print("Your guess number is too small.Guess Again...")
    else:
        print("Your guess number is too big.Guess Again...")
    
print("--------------GAME OVER---------------")    