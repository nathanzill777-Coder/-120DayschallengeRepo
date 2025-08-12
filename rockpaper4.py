emojis = { 'r': '🪨' , 's': '✂️', 'p':'📄'}
choices = ['r','p','s']

import random
while True:
    user_choice = input(str("Please:press R for rock, S for Scissors and P for paper\n")).strip().lower()
    if user_choice not in choices:
        print("INVALID choice!")
        continue

    computer_choice = random.choice(choices)   

    print(f"You choose{emojis[user_choice]}")
    print(f"computer choose {emojis[computer_choice]}") 

    if user_choice == computer_choice:
        print("IT's a draw")
    elif ((user_choice == 'r'and computer_choice == 's') or 
    (user_choice =='p' and computer_choice == 'r') or 
    (user_choice =='s' and computer_choice == 'p')):
        print("YOU WIN!!")
    else:
        print("YOU LOSE!!")
        
    play_again = input("Do you want to continue (y/n)?")
    if play_again == "n":
            break
#if not
#terminate.