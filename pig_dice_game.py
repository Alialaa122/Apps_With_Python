#First we need to decide which is player turn 1 or 2 
# then play a dice for once if it is one then the score that he has will be zero 
# if it is not then ask the player if he wants to continue playing 
# so if it is yes then keep playing
# if it is no then calculate the dice score that he made 
# and show the current scores
# then go to another player 
# and if the total score was 40 points then we determine the winner and exit the program
 


import random
dice=[1,2,3,4,5,6]
score1=0
score2=0
turn=1


target_score=int(input("Enter Target score do you wanna to reach: "))



while(score1<target_score and score2<target_score):
    print(f"player {turn}'s turn")
    score=0
    while True:
        roll=random.choice(dice)
        print(f"You rolled a {roll}")
        if roll==1:
            print("You lost All Your Points :(")
            score=0
            break
        
        score+=roll
            
        continuation=input("Roll again (y/n): ").strip().lower()
        if continuation=="n":
            break

    if turn==1:
        score1+=score
        print(f"You scored {score} this turn")
        print(f"Current scores: player 1: {score1}, player 2: {score2}")
        turn=2
    else:
        score2+=score
        print(f"You scored {score} this turn")
        print(f"Current scores: player 1: {score1}, player 2: {score2}")
        turn=1


if score1==target_score:
    print("Player1 wins")
else:
    print("player 2 wins")





