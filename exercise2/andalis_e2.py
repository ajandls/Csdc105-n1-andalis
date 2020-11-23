
   # Author          : Ariane Jane J. Andalis
   # Course and Year : BS Information Technology - 2nd year
   # Filename        : andalis_e2.py
   # Description     : A program that prints some info about myself with the use of Python data structures.
   # Honor Code      : I have not given nor received any unathorized help in
   #                   completing this exercise. I am also well aware of the 
   #                   policies stipulated in the AdNU student handbook.

data = { 'name' : 'Ariane Jane J. Andalis', 'spirit_animal' : 'Hummingbird', 'reason' : 'I am adaptable, resilient and I would also like to travel to great distances.', 'hobbies' : [ 'Cook and Bake', 'Read books', 'Ride a bike' ] , 'dream': 'UI/UX Designer, an Entrepreneur, and a Triathlete' }
   
for name in list(data.get("name")):
	print("I am", data['name'])
	break

for spirit_animal in list(data.get("spirit_animal")):
	print("My spirit animal is a", data['spirit_animal'],',')
	break

for reason in list(data.get("reason")):
	print("because", data['reason'])
	break

print("When not in school, I love to: ")	
for hobbies in list(data.get("hobbies")):
	print("*", hobbies.split(","))
    
for dream in list(data.get("dream")):
	print("I dream of being a", data['dream'], "in the future.")
	break
