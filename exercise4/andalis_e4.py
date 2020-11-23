# Author          : Ariane Jane J. Andalis
# Course and Year : BS Information Technology - 2nd year
# Filename        : andalis_e4.py
# Description     : The main file for Heron's Formula.
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.

from geometry import math, perimeter, triangle_heronsarea, condition_checker

a, b, c = input("Enter the sides of the triangle: ").split()

a = float(a)
b = float(b)
c = float(c)

x = condition_checker(a, b, c)

if x == True:
    print("Perimeter: ",'%.2f'%perimeter(a, b, c))
    print("Area: ", '%.2f'%triangle_heronsarea(a, b , c))
else:
   print("Error: Invalid Input")
