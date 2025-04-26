# Ask user for a filename to open or create
# if  this file doesnot exist then create one with this name
# if this file exist then go to next step

# Ask user to Enter text and type save in a new line to exit

import os
import re
os.chdir(os.path.dirname(os.path.abspath(__file__)))

user_file=input("Enter the filename to open or create:").strip()
dirpath=r"C:\Users\HP\Documents\projects"
# filename=f"{dirpath}\{user_file}"
#              =
filename=os.path.join(dirpath,user_file)

f=open(filename)
# user_word=input("Enter the word do you want to search: ").strip()

# content=f.read()

# search=re.search(user_word,content)

# print(search)

# if search:
#     print("ok")
# else:
#     print("Not ok")

# print(content)




    


def file_checker():

    if not os.path.exists(filename):
        print(f"{user_file} not found",end=" ")
        print("Creating the file")
        open(filename,"x").close() 

    else:
        print("Opening the file to write")

def choice():
    user_ask=input("Do you want overwrite or append new text (o=> overwrite,a=>append): ").strip().lower()
    try:
        if user_ask=="a":
            return "a"
        elif user_ask=="o":
            return "w"
        else:
            return "a"
    except ValueError:
        print("Please Enter A valid character")





def editor():

    mode=choice()
    print("Enter Your Text (Type 'SAVE' on a new line to save and exit): ")
    try:
        with open(filename,mode) as f:
            while True:
                    user_input=input()
                    if user_input.lower()=="save":
                        print(f"{user_file} saved.")
                        break
                    f.write(user_input+"\n")

    except Exception as e:
        print(f"Error {e}")
    
file_checker()
editor()










