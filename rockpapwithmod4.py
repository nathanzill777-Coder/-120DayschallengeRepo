emojis = { 'r': '🪨' , 's': '✂️', 'p':'📄'}
choices = ['r','p','s']
#Modularizing means chunking codes of similar functionality
#into a same function. we are deducing number of code.
import random
def get_user_choice():
    while True:
        user_choice = input(str("Please:press R for rock, S for Scissors and P for paper\n")).strip().lower()
        if user_choice in choices:
            return user_choice
        else:
             print("INVALID CHOICE!")

def display_choice(user_choice, computer_choice):
    print(f"You choose{emojis[user_choice]}")
    print(f"computer choose {emojis[computer_choice]}")

def select_winner(user_choice, computer_choice):

        if user_choice == computer_choice:
            print("IT's a draw")
        elif ((user_choice == 'r'and computer_choice == 's') or 
    (user_choice =='p' and computer_choice == 'r') or 
    (user_choice =='s' and computer_choice == 'p')):
            print("YOU WIN!!")
        else:
             print("YOU LOSE!!")         

def play_game(): 
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)  

        display_choice(user_choice,computer_choice) 

        
        select_winner(user_choice,computer_choice)
            
        play_again = input("Do you want to continue (y/n)?")
        if play_again == "n":
                break
play_game()