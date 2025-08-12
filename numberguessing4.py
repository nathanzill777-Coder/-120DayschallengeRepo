#Number guessing game.

import random

number = random.randint(1,100)
while True:
    try:
            ask = int(input("Esteemed user, please guess the number"))
            if ask < number:
                print("Too low")
            elif ask > number:
                print("Too high")
            else:
                print("Congratulations,you succesfully guesses the number")
                break
    except ValueError:
         print("Please Enter a valid choice")
        
    