# Author          : Ariane Jane J. Andalis
# Course and Year : BS Information Technology - 2nd year
# Filename        : geometry.py
# Description     : Heron's Formula to find the area and perimeter of the triangle.
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.

import math

def perimeter(*side_lengths):
    sum = 0
    for i in side_lengths:
        sum = sum + i
    return sum 

def triangle_heronsarea(a, b, c):
    s = perimeter(a, b, c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def condition_checker(a, b, c):
    if a + b > c:
    	return True
    else:
    	return False
