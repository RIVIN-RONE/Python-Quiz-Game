import random

random=random.randint(1,100)

while True:
    userChoice=int(input("Enter your guess: "))
    if(userChoice==random):
        print("Success: You have entered the right choice")
        break
    elif(userChoice>random):
        print("You need to guess a lesser number")
    elif(userChoice<random):
        print("you need to guess a bigger number")
    else:
        print("Invalid entry!!!")     
print("---GAME OVER---")           