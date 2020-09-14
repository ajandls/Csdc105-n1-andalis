# Author          : Andalis, Ariane Jane J.
# Course and Year : 2 - BS IT
# Filename        : andalis-probb.py
# Description     : A program that reads an integer n and prints the sequence F_n of Fibonacci numbers as a comma-separated list on a single line.
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.

T = int(input("")) #user-input test cases
while (T > 0):
	n = int(input("")) #takes input from user
	firstElem = 0 #first element
	secElem = 1 #second element
	counter = 1
	x = 1
	print("CASE {}: ".format(x), end="")

#process
	if (counter < n):
		print(firstElem, secElem, end = " ")
		for x in range(1, n):
			nextNum = firstElem + secElem                  
			print(nextNum, end = " ")
			firstElem = secElem
			secElem = nextNum
			#n = n + 1
	else:
		print("Please enter a positive number.")
	T = T - 1
	print(" ")
