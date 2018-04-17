from time import sleep
board = [["_","_","_"],["_","_","_"],["_","_","_"]]

letter_1 = str.upper(input("Who goes first? X or O? "))
letter_2 = "O"
if (letter_1 == str.upper("x")):
    letter_2 = "O"
elif (letter_1 == str.upper("o")):
    letter_2 = "X"


def display():
    #This function sets all the conditions
    #  for winning. Can you create a code that can
    #simplify this entire block into something smaller?
    for i in range(3):
        print(" ".join(board[i]))
    if (board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X"):
        print("Player X wins!")
        exit(0)
    elif (board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O"):
        print("Player O wins!")
        exit(0)
    elif (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X"):
        print("Player X wins!")
        exit(0)
    elif (board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O"):
        print("Player O wins!")
        exit(0)
    elif (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X"):
        print("Player X wins!")
        exit(0)
    elif (board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O"):
        print("Player O wins!")
        exit(0)

    elif (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X"):
        print("Player X wins!")
        exit(0)
    elif (board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O"):
        print("Player O wins!")
        exit(0)
    elif (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X"):
        print("Player X wins!")
        exit(0)
    elif (board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O"):
        print("Player O wins!")
        exit(0)
    elif (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X"):
        print("Player X wins!")
        exit(0)
    elif (board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O"):
        print("Player O wins!")
        exit(0)

    elif (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X"):
        print("Player X wins!")
        exit(0)
    elif (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O"):
        print("Player O wins!")
        exit(0)

    elif (board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X"):
        print("Player X wins!")
        exit(0)
    elif (board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O"):
        print("Player O wins!")
        exit(0)


def Pick_Function():
    display()
    counter = 8
    while (counter > 0):
        if(counter%2 == 0):
            letter = letter_1
        elif(counter%2 == 1):
            letter = letter_2
        sleep(.5)
        print("Turn "+letter)
        sleep(0.5)
        num10 = int(input("What row? "))
        if (num10 <= 0 or num10 >=4):
            counter3 = 1
            while (counter3 > 0):
                num10 = int(input("This number is out of bounds. Try again. "))
                if (num10 > 0 and num10 < 4):
                    counter3 = 0

        sleep(0.2)
        num20 = int(input("What column? "))
        if (num20 <= 0 or num20 >= 4):
            counter4 = 1
            while(counter4 > 0):
                num20 = int(input("This number is out of bounds. Try again. "))
                if (num20 > 0 and num20 < 4):
                    counter4 = 0
        num1 = int(num10 - 1)
        num2 = int(num20 -1)

        if(board[num1][num2] == "X" or board[num1][num2] == "O"):
            print("This has been picked already. Pick another spot.")
            counter +=1
        board[num1][num2] = board[num1][num2].replace("_", str(letter))
        display()
        counter -= 1
        print(counter)
        if (counter == 0):
            print("Well. It seems there is a tie...")
            sleep(.5)
            print("Congratulations! Neither of you won.")
            exit(0)


Pick_Function()
