# NAME  : Harshith G
# USN   : 25BTRAD040
# BRANCH: CSE – AIDE A
# LAB EXPERIMENT - 2
# Lab Exercise 5: Number Guessing Game

import random

number = random.randint(1, 100)

print("Number Guessing Game")
print("Guess a number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
        break
