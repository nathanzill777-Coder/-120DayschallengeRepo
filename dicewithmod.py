#Program Modifications:[Optional]

#Modify the program so the user can specify how many dice they want to roll.
#Add a feature that keeps track of how many times the user has rolled the dice during the session.
#This will require a counter that increments each time the dice are rolled.



import random

count = 0

while True:
    ask = input("Do you want to play? Press 'y' for yes and 'n' for no: ").strip().lower()
    if ask == "y":
        try:
            number = int(input("Please enter the number of dice you wish to use: ").strip())
        except ValueError:
            print("That's not a valid number. Try again.")
            continue

        results = []
        for i in range(number):
            roll = random.randint(1, 6)
            results.append(roll)
            print(f"Dice {i+1} rolled: {roll}")
        
        count += 1
        print(f"You played {count} time(s) so far.\n")

    elif ask == "n":
        print("Thank you for playing!")
        print(f"You played {count} time(s) total.")
        break

    else:
        print("Invalid choice. Please enter 'y' or 'n'.")
