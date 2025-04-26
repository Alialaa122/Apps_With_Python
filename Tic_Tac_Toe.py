
board=[[" "," "," "],
            [" "," "," "]
            ,[" "," "," "]]
players=["O","X"]

o_counter=0
x_counter=0
draws=0



def is_draw(board):
    return all(cell !=" " for row in board for cell in row)

def stats(player,draw=False):
    global o_counter,x_counter,draws
    if draw:
        draws+=1
    elif player=="O":
        o_counter+=1
    elif player=="X":
        x_counter+=1

    print("Stats: ")
    print(f"Player O wins: {o_counter}")
    print(f"Player X wins: {x_counter}")
    print(f"Draw: {draws}")

def display_board(board_list):
    print("---+---+---")
    print(f" {board_list[0][0]} | {board_list[0][1]} | {board_list[0][2]}  ")
    print("---+---+---")
    print(f" {board_list[1][0]} | {board_list[1][1]} | {board_list[1][2]}  ")
    print("---+---+---")
    print(f" {board_list[2][0]} | {board_list[2][1]} | {board_list[2][2]}  ")
    print("---+---+---")


def check_winner(board_list,player):
    for row in board_list:
        if all(cell==player for cell in row):
            print(f"{player}'s Wins")
            return True
        
    for col in board_list:
        if all(cell==player for cell in col):
            return True
    
    if all(board_list[i][i]==player for i in range(3)):
        return True
    
    if all(board_list[i][2-i]==player for i in range(3)):
        return True
    
    return False



def game():

    global board
    board=[[" "," "," "],
            [" "," "," "]
            ,[" "," "," "]]

    while True:
        for player in players:
            display_board(board)
            print(f"Player {player}'s turn")

            while True:
                try:
                    row=int(input("Enter row (0-2): "))
                    col=int(input("Enter column (0-2): "))
                    if 0<=row<3 and 0<=col<3 and board[row][col]==" " :
                        break
                    else:
                        print("Invalid Move Please Try Again")
                
                except ValueError:
                    print("Please, Enter a Valid Number")

            board[row][col]=player
            if check_winner(board,player):
                print(f"{player}'s Wins")
                stats(player)
                continuation()
                
            if is_draw(board):
                stats(draw=True)
                continuation()



def continuation():
        result=input("Do You Wanna Play Another Game? (y/n)").strip().lower()
        if result=="n":
            print("Thanks For Playing")
            exit()
        elif result=="y":
            game()
        else:
            print("Invalid Input Please Enter y or n")
            


game()


