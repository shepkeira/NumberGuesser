from random import randint
import math


def pick_number():
    print("Pick your number. But don't tell me yet!")
    high = 100
    low = 0
    guess = math.floor((high - low) / 2 + low)
    while True:
        print("Is the number ", guess)
        ans = input("A - Correct, B - Too High, C - Too Low")
        if ans == "A":
            print("I Win!")
            break
        elif ans == "B":
            high = guess
            guess = math.floor((high - low) / 2 + low)
        else:
            low = guess
            guess = math.floor((high - low) / 2 + low)


def guess_number():
    num = randint(0, 100)
    while True:
        guess = int(input("Pick a number between 0 and 100: "))
        if num == guess:
            print("Correct!")
            break
        elif num > guess:
            print("Too low guess again")
        else:
            print("Too high guess again")


#print("Do you want to guess a number or pick a number for me to guess?")

# while True:
#     print("A - Guess a number")
#     print("B - Pick a number")
#     choice = input("What would you like to do? ")
#
#     if choice == "A":
#         guess_number()
#     elif choice == "B":
#         pick_number()
#     else:
#         print("That is not an option try again")
