# NAME  : Harshith G
# USN   : 25BTRAD040
# BRANCH: CSE – AIDE A
# LAB EXPERIMENT - 1
# Lab Exercise 3: Programs Using Variables, Operators and Input/Output

# ---------- (a) Sum and Product ----------
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)
print("Product =", a * b)

# ---------- (b) Simple Interest ----------
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

si = (p * r * t) / 100
print("Simple Interest =", si)
