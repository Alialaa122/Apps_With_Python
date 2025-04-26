#Ask user to chose from rock,paper or scissors
#if he types anything instead 
# print an error
#if he chose r/p/s:
# then make a random choice for a computer between those three choices
#then check who wins
#then ask user if he wants to continue or not 
#if yes then repeat the process
#if no then terminate


import random
import emoji

choices=["r","p","s"]
emojis={"p":emoji.emojize("📄"),"r":emoji.emojize("🪨"),"s":emoji.emojize("✂️")}



def get_user_choice():
        
        while True:
            choice=input("Rock, Paper or Scissors? (r/p/s)").strip().lower()
            if choice in choices:
                return choice
            else:
                print("Invalid Input")

def display_emoji(choice,computer_choice):
        
        print(f"You Chose {emojis[choice]}")
        print(f"Computer Chose {emojis[computer_choice]}")


def best_of_three(com_wins,user_wins):
     while True:
        if com_wins==2:
            print("Computer Wins The Game")
        elif user_wins==2:
            print("You Win The Game")
        else:
             break


def determine_winner(choice,computer_choice):
                
        if ((choice=="r"and computer_choice=="s") or
        (choice=="p"and computer_choice=="r") or
        (choice=="s"and computer_choice=="p")):

            display_emoji(choice,computer_choice)
            print("You Win!")



        elif ((computer_choice=="r"and choice=="s") or
        (computer_choice=="p"and choice=="r") or 
        (computer_choice=="s"and choice=="p")):

            display_emoji(choice,computer_choice)

            print("You Lose!")
        else:
            display_emoji(choice,computer_choice)
            print("Draw")

        
                 
def play_game():

    user_wins=0
    com_wins=0

    while True:
            choice=get_user_choice()
            computer_choice=random.choice(choices)
            determine_winner(choice,computer_choice,user_wins,com_wins)

            continuation=input("Continue? (y/n): ").strip().lower()
            if continuation=="y":
                continue
            elif continuation=="n":
                break
                    
play_game()