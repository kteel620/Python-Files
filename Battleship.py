from random import randint
print("Welcome to Battleship!")
board = []

row = ["0"]*5
col = "".join(row)

print("You have three chances to sink the hidden ship.")
a = int(len(row) - 1)
ans_col = randint(0,a)
ans_row = randint(0,a)
print(ans_col,ans_row)


for x in range(5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

counter = 3
while (counter > 0):
    guess_col = int(input("Guess which column the ship is hiding in. "))
    guess_row = int(input("Guess which row the ship is hiding in. "))
    real_guess_col = guess_col - 1
    real_guess_row = guess_row - 1
    if ((real_guess_col == ans_col) and (real_guess_row == ans_row)):
        print("Congratulations! You got my ship! ")
        exit()
    elif ((real_guess_col < 0) or (real_guess_col > a) or (real_guess_row < 0) or (real_guess_col > a)):
        print("That's not even in the ocean.")
        counter -= 1
    elif (board[real_guess_col][real_guess_row] == "X"):
        print("You guessed this already. ")
    elif((real_guess_col != ans_col) or (real_guess_row != ans_col)):
        counter -= 1
        board[real_guess_col][real_guess_row] = "X"
        print_board(board)
        if (counter == 1):
            print("You have one try left. ")
        else:
            print("Incorrect answer. You have " + str(counter) + " tries left. ")








