board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def show_board():
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])

player = "X"

for i in range(9):
    show_board()
    
    pos = int(input("Enter position (0-8): "))
    
    if board[pos] == "-":
        board[pos] = player
    else:
        print("Place already filled")
        continue
    
    if player == "X":
        player = "O"
    else:
        player = "X"

show_board()
print("Game Over")