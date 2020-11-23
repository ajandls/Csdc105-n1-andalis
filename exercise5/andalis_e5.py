# Author          : Ariane Jane J. Andalis
# Course and Year : BS Information Technology - 2nd year
# Filename        : andalis_e5.py
# Description     : Dice using Python's classes and objects.
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.

import random

from dice import dice, Tetrahedron  

d = dice()                         
print(d)
                             
for i in range(5):                   
	d.roll()     
