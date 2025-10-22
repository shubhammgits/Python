import random

genNum = random.randint(1,10)

tries = 0

while True:
    userNum = int(input("Guess the number between 1 to 10 : "))

    if userNum == genNum:
        tries+=1
        print(f"You are right! you guessed the number in {tries} tries")
        break

    elif userNum > genNum:
        print("Guess the lesser number!")
        tries+=1
    
    elif userNum < genNum:
        print("Guess the bigger number!")
        tries+=1

    else:
        tries+=1
        print("You are wrong!")
