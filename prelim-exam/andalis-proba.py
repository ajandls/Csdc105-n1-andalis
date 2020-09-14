# Author          : Andalis, Ariane Jane J.
# Course and Year : 2 - BS IT
# Filename        : andalis-proba.py
# Description     : A program that prints a triangle shape composed of specific ASCII character.
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.

T = int(input("")) #user-input test cases

while (T > 0):
	k, c = input().split() #process that splits the height of the triangle and the character from user-input
	x=1
	print("CASE {} :".format(x))
	
	k = int(k)
	for i in range(1, k+1):
		for j in range(-1, k-i+1):
			print(end = " ")
		for j in range(i, 1, -1): #in charge of the left side of the triangle
			print(c, end = " ")
		for j in range(1, i+1): #in charge of the right side of the triangle
			print(c, end = " ")
		print(" ")
	T = T-1
	print()
