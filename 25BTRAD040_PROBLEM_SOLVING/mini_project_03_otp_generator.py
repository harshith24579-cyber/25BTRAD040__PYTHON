# NAME  : Harshith G
# USN   : 25BTRAD040
# BRANCH: CSE – AIDE A
# MINI PROJECT - 2
# Program 3: OTP Generator

import random

print("===== OTP GENERATOR =====")

otp = random.randint(100000, 999999)

print("Your OTP is:", otp)

user_otp = int(input("Enter the OTP: "))

if user_otp == otp:
    print("OTP Verified Successfully!")
else:
    print("Invalid OTP!")

# ---------------------------------------------------------------
# Student Grading Automation
