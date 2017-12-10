"""Project asking the user to guess a number between 1 and 20, then letting the user know if they
are close or not. Person gets three tries. They cannot guess the same number."""

from random import randint
from time import sleep

Computer_pick = randint(1,20)
print(Computer_pick)

start = True

count = 3

band_nums = []
close1 = Computer_pick - 3
close2 = Computer_pick + 3

def counter(something):
    a = str(something)
    if (something == 1):
        print("You have one try left")
    else:
        print("You have " + a + " tries left.")

while (start == True):
    print(band_nums)
    my_ans = input("Pick an integer between 1 and 20 inclusive. ")
    my_answer = int(my_ans)

    if (my_answer < 1 or my_answer > 20):
        print("Your number is out of range. Guess again. ")
        continue

    elif (Computer_pick != my_answer):

        if (my_answer in range(close1, close2)):
            if (my_answer in band_nums):
                print("You guessed that already!")
                continue
            else:
                count -= 1
                band_nums.append(my_answer)
                sleep(1)
                if (count == 0):
                    print("You lose")
                    start = False
                else:
                    counter(count)
                    print("Guess again. You're close. ")
                continue

        else:
            if (my_answer in band_nums):
                print("You guessed that already!")
                continue
            else:
                count -=1
                band_nums.append(my_answer)
                sleep(1)
                if (count == 0):
                    print("You lose")
                    start = False
                else:
                    counter(count)
                    print("Guess again. ")
                continue

    elif (Computer_pick == my_answer):
        print("Congratulations! By some miracle, you guessed right!")
        start = False




