# CSCI1010: Lab 1, Problem 1
# Filename: hw1pr2.py
# Name: Samuel Otto
# Problem description: Solving the quadratic equation!

from math import *

posX = 0
negX = 0

a = float(input("Supply an input for a: "))
b = float(input("Supply an input for b: "))
c = float(input("Supply an input for c: "))

square = float((b*b) - (4 * a * c))
print(square)

negX = ( (-1 * b) - sqrt(square)) / (2 * a)
posX = ( (-1 * b) + sqrt(square)) / (2 * a)
print("The solution for x are", negX, "and", posX)