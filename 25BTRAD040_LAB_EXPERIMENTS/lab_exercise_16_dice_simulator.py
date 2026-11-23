# NAME  : Harshith G
# USN   : 25BTRAD040
# BRANCH: CSE – AIDE A
# LAB EXPERIMENT - 5
# Lab Exercise 16: Dice Simulator Using random Module

import random


def dice_simulator():
    while True:
        print("\n1. Roll One Die")
        print("2. Roll Two Dice")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            result = random.randint(1, 6)
            print("Dice result:", result)
        elif choice == "2":
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            print("First die:", die1)
            print("Second die:", die2)
            print("Total:", die1 + die2)
        elif choice == "3":
            print("Dice simulation ended.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    dice_simulator()
