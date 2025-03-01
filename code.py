import random

target = random.randint(1,100)

while True:
    userChoice = input("Guess the target or Quit: ")
    if(userChoice == "Quit"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess!!")
        break
    elif(userChoice < target):
        print("Your number is too low. Take a bigger number...")
    else:
        print("Your number is too big. Take a smaller number...")


print("_____GAME OVER______")
