import numpy as np
import math


def getguess():
    a = input("Enter the guess number: ")

    while not a.isnumeric():
        print("Enter the valid number")
        a = input("Valid number please\n")
    a = int(a)

    return a


def check(guess, value):
    count = 0
    while count <= 3:
        if guess == value:
            print("CONGO !! YOU WIN :)")
            break
        elif guess < value:
            print("higher")
            guess = getguess()
            count = count + 1
        elif guess > value:
            print("lower")
            guess = getguess()
            count = count + 1
    else:
        print("OH YOU LOOSE :(")


print("levels--> 1.Easy      2.Medium      3.Hard      4.Expert")
print("Enter (1-4) for levels .")
while True:
    level = input()
    try:
        level = int(level)
        if not (1 <= level <= 4):
            print("Enter value between (1-4).")
        else:
            break

    except:
        print("Invalid input .")

match level:
    case 1:
        print("You have choosen easy level.")
        print("Range of number is (1-10) ")

    case 2:
        print("You have choosen medium  level.")
        print("Range of number is (10-100) ")

    case 3:
        print("You have choosen hard level.")
        print("Range of number is (100-1000) ")
    case 4:
        print("You have choosen expert level.")
        print("Range of number is (1000-10000) ")


guess = getguess()

value = np.random.randint(1 * 10 ** (level - 1), (1 * 10**level) + 1)
check(guess, value)
