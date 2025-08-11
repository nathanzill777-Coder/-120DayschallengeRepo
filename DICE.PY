#Write a program that simulates rolling a pair of dice. Each time the program runs, it should randomly
#generate two numbers between 1 and 6(inclusive). representing the result of each dice. the program should 
#then display the results and ask if the user would like to roll again
import random
while True:
      choice = input(str("Estemmed user: Do you wish to play the game? Press y for yes and n for no.")).strip().lower()
      if choice == "y":
         dice1 =random.randint(1,6)
         dice2 =random.randint(1,6)
         print("The values of dice1 and dice2 respectively are {} and {}".format(dice1,dice2))
      elif choice == "n":
         print("Thank you for being with us and playing esteemed user.")
         break
      

#Program Modifications:[Optional]
#Modify the program so the user can specify how many dice they want to roll.
#Add a feature that keeps track of how many times the user has rolled the dice during the session.
#This will require a counter that increments each time the dice are rolled. 