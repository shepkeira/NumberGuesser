from tkinter import *
from tkinter import ttk
import math
from random import randint

top = Tk()
content = ttk.Frame(top, padding=(5,5,5,5))
content.grid(column=0, row=0)


def clear(object):
    slaves = object.grid_slaves()
    for x in slaves:
        x.destroy()

global num
num = 0
global high
high = 100
global low
low = 0
global guess
guess = math.floor((high - low) / 2 + low)


def TooHigh():
    global high
    global guess
    global low
    clear(content)
    high = guess
    guess = math.floor((high - low) / 2 + low)
    next_guess()


def TooLow():
    global high
    global guess
    global low
    clear(content)
    low = guess
    guess = math.floor((high - low) / 2 + low)
    next_guess()


def Correct():
    clear(content)
    win_label = ttk.Label(content, text="I win!")
    win_label.grid(column=0, row=0)


def pick_number():
    global guess
    clear(content)
    Initial_text = ttk.Label(content, text="Pick your number. But don't tell me yet!")
    Initial_text.grid(column=0, row=0, columnspan=3)
    Guess = ttk.Label(content, text="Is the number " + str(guess) + "?")
    Guess.grid(column=0, row=1, columnspan=3)
    High = ttk.Button(content, text="Too High", command=TooHigh)
    High.grid(column=1, row=2)
    Low = ttk.Button(content, text="Too Low", command=TooLow)
    Low.grid(column=2, row=2)
    Correct_button = ttk.Button(content, text="Correct!", command=Correct)
    Correct_button.grid(column=3, row=2)


def next_guess():
    global guess
    clear(content)
    Guess = ttk.Label(content, text="Is the number " + str(guess) + "?")
    Guess.grid(column=0, row=0, columnspan=3)
    High = ttk.Button(content, text="Too High", command=TooHigh)
    High.grid(column=1, row=1)
    Low = ttk.Button(content, text="Too Low", command=TooLow)
    Low.grid(column=2, row=1)
    Correct_button = ttk.Button(content, text="Correct!", command=Correct)
    Correct_button.grid(column=3, row=1)


def correct():
    clear(content)
    correct_label = ttk.Label(content, text="You Win!")
    correct_label.grid(column=0, row=0)


def number_choosen(user_guess, num):
    if num == user_guess:
        correct()
    elif num > user_guess:
        guess_low(num)
    else:
        guess_high(num)


def guess_high(num):
    clear(content)
    user_guess = IntVar()
    high_label = ttk.Label(content, text="Too High, Guess Again")
    high_label.grid(column=0, row=0)
    guess_entry = ttk.Entry(content, textvariable=user_guess)
    guess_entry.grid(column=0, row=1)
    confirm_button = ttk.Button(content, text="Enter", command=lambda: number_choosen(user_guess.get(), num))
    confirm_button.grid(column=1, row=1)
    guess_entry.bind("<Return>", (lambda event: number_choosen(user_guess.get(), num)))


def guess_low(num):
    clear(content)
    user_guess = IntVar()
    low_label = ttk.Label(content, text="Too Low, Guess Again")
    low_label.grid(column=0, row=0)
    guess_entry = ttk.Entry(content, textvariable=user_guess)
    guess_entry.grid(column=0, row=1)
    confirm_button = ttk.Button(content, text="Enter", command=lambda: number_choosen(user_guess.get(), num))
    confirm_button.grid(column=1, row=1)
    guess_entry.bind("<Return>", (lambda event: number_choosen(user_guess.get(), num)))


def guess_number():
    clear(content)
    num = randint(0, 100)
    user_guess = IntVar()
    initial_text = ttk.Label(content, text="Guess a number between 0 and 100: ")
    initial_text.grid(column=0, row=0, columnspan=2)
    guess_entry = ttk.Entry(content, textvariable=user_guess)
    guess_entry.grid(column=0, row=1)
    confirm_button = ttk.Button(content, text="Enter", command=lambda: number_choosen(user_guess.get(), num))
    confirm_button.grid(column=1, row=1)
    guess_entry.bind("<Return>", (lambda event: number_choosen(user_guess.get(), num)))


def main():
    clear(content)
    text_label = ttk.Label(content, text="Would you like to pick a number or guess a number?")

    pick_button = ttk.Button(content, text="Pick", command=pick_number)
    guess_button = ttk.Button(content, text="Guess", command=guess_number)

    text_label.grid(column=0, row=0, columnspan=2, padx=5, pady=5)
    pick_button.grid(column=0, row=1, padx=5, pady=5)
    guess_button.grid(column=1, row=1, padx=5, pady=5)


main()
top.mainloop()