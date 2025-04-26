

# While user doesnot choose  4 (exit) we keep display menu

# Display todo list menu for user with 4 options

# once program started the file should load with previous 
# 1 view task this function is to display tasks that the user has
# if he hasnot tasks we can ask him if he wants to add ones or not 
# if yes we call add a task function if not we go back to todo list menu

# 2 add a Task this function is to ask user to add an new task

# 3 remove a task this function is to make user able to remove any task in the list

# 4 exit the program

import os

options=["1","2","3","4","5"]

filepath=r"C:\Users\HP\Documents\projects\To-Do_list.txt"

def display_todo_list_menu():
    print("Todo List Menu: ")
    print("1. View Tasks ")
    print("2. Add a Task ")
    print("3. Remove a Task" )
    print("4. Mark a Task" )
    print("5. Exit  ")







def load_file():

    if  not os.path.exists(filepath):
        return []

    with open(filepath,mode="r",encoding="utf-8") as file:
        return[line.strip() for line in file.readlines()]


def save_file(todo_list):

    with open(filepath,mode="w",encoding="utf-8") as file:
        for index,task in enumerate(todo_list,1):
            file.write(f"{task} \n")



def add_task(todo_list):

    new_task=input("Enter a new task: ").strip()
    if new_task in todo_list:
        print("This Task is Already Added")
    else:
        todo_list.append(new_task)
        print("The Task is Added")

def view_tasks(todo_list):

    if  not todo_list:
        print("To-Do_list is empty")
        user_input=input("Do You Wanna add a task?(y/n)").strip().lower()
        if user_input=="y":
            add_task(todo_list)
        return

    else:
        print("\nYour Tasks:")
        for index,task in enumerate(todo_list,1):
            print(f"Task {index} => {task}")


        
        

def mark_task(todo_list):

    view_tasks(todo_list)
    if not todo_list:
     return 

    task_number=int(input("Enter the number of the task did you finsh?"))
    try:
        if 1<=task_number<=len(todo_list):

            todo_list[task_number-1]=f"✅ {todo_list[task_number-1]}"
        else:
            print("Invalid Task_Number")
    except ValueError:
        print("Please Enter a Valid Number")

        
    



def remove_task(todo_list):

    view_tasks(todo_list)
    if todo_list==[]:
        return 

    task_number=int(input("Enter the number of the task do you want to remove"))
    try:
        if 1<=task_number<=len(todo_list):
            removed_task=todo_list.pop(task_number-1)
            print(f"Task {removed_task} removed.")

        else:
            print("Invalid Task_Number")
    except ValueError:
        print("Please Enter a Valid Number")






def program():

    todo_list=load_file()

    while (True):
        display_todo_list_menu()
        user_choice=input("Enter Your choice: ")

        if user_choice not in options:
            print("Invalid Option Please Try Again")
            continue
        
        if user_choice=="1":
            view_tasks(todo_list)
        elif user_choice=="2":
            add_task(todo_list)
        elif user_choice=="3":
            remove_task(todo_list)
        elif user_choice=="4":
            mark_task(todo_list)
        elif user_choice=="5":
            print("Exit the program")
            save_file(todo_list)
            break




program()

