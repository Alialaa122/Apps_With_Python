# Number Guessing Game 


#Ask user for a number between 1 and 100
#loop
    # if he doesnot type a number
    # print an alert to type a valid number
    # create a random number between 1 and 100
    # if typed number > random number 
    # print("Too High")
    # if typed number< random number
    # print("Too Low")
    # if he types the right number 
    # print("Congartulations!")


import random

random_num=random.randint(1,100)
while True:

    try:
        guess=int(input("Enter A Number (Between 1 and 100): "))
        
        if guess > random_num:
            print("too high")
        elif guess < random_num:
            print("too low")
        else:
            print("Congratulations! You Guessed The right Number")
            break

    except ValueError:
        print("Enter A Valid Number")






# Optional Enhancements

import random

try:
    minimum=int(input("Enter The minimum range: "))
    maximum=int(input("Enter The maximum range: "))
    random_num=random.randint(minimum,maximum)
except ValueError:
    print("Plese Enter A valid range")


attempts=0
best_score=0

while attempts != 5:

    try:


        guess=int(input(f"Enter A Number (Between {minimum} and {maximum}): "))
        
        if guess > random_num:
            print("too high")
            attempts+=1
        elif guess < random_num:
            print("too low")
            attempts+=1
        else:
            print("Congratulations! You Guessed The right Number")
            print(f"The Best Score is: {attempts} attempts.")
            break

    except ValueError:
        print("Enter A Valid Number")

else:
    print("Sorry You have finished Your 5 Attempts")
    print(f"The right Number is {random_num} ")




