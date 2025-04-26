# Dice Rolling Game

# import random
# while  True:
#     user_input=input("Roll The dice? (y/n): ").strip().lower()
#     if user_input=="y":
            
#             num1=random.randint(1,6)
#             num2=random.randint(1,6)
#             print(f"({num1},{num2})")
            

#     elif user_input=="n":
#             print("Thanks for playing!")
#             break

#     else:
#            print("Ivalid Choice!")


# Optional Enhancements

import random

counter=0
number=int(input("How Many dice do you want to roll?"))

while  number!=0:

    user_input=input("Roll The dice? (y/n): ").strip().lower()
    if user_input=="y":

            num1=random.randint(1,6)
            num2=random.randint(1,6)
            print(f"({num1},{num2})")
            counter+=1
            number-=1
            

    elif user_input=="n":
            print("Thanks for playing!")
            break

    else:
        print("Invalid Choice!")

print(f"The number of rolled dice is {counter} times.")


      
   






           
            
