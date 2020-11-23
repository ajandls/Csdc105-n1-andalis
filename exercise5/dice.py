# Author          : Ariane Jane J. Andalis
# Course and Year : BS Information Technology - 2nd year
# Filename        : dice.py
# Description     : Dice using Python's classes and objects.
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.

import random  
                               
class dice:                                   
    def __init__(self, sides = 6):            
        self.sides = sides                     
	
    def roll(self):            
        print(random.randint(1, 6))  
	
    def __str__(self):                         
        return "DICE: {}".format(self.sides)   

class Tetrahedron(dice):                      
    def __init__(self, sides):                 
        self.sides = sides    
 
    def roll(self):            
        print(random.randint(1, 4))  
			
    def __str__(self):                         
        return "DICE: {}".format(self.sides)
