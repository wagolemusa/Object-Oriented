"""
Bellow your existing code, define a function called plane_ride_cost 
that takes a string city as input.

the fuction should return a difirrent price depending on the location,
Below are the valid destination and their corresponding rounds tips prices
Use if else
"Nairobi": 183
"Kisumu t0 busia": 400
"Mombasa to kericho": 3000

"""

def plane_ride_cost(city):
	if city == "Nairobi":
		return "2000"
	elif city == "Kisumu":
		return "400"
	elif city == "Mombasa":
		return "3000"
	elif city == "busia":
		return 500
# plane_ride_cost = input('please enter the city')
print(plane_ride_cost('Nairobi'))