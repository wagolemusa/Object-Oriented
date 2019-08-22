
"""
Bellow your existing code, define a function called
trip_cost that takes two arguments city and days.
Function should return the sum of calling the rental_car_cost(days)
hotel_cost(days) and plane_ride_cost(days)
"""
def hotel_cost(nights):
	per_night_rate = 140 
	return per_night_rate * nights


def plane_ride_cost(city):
	if city == 'Charlptte':
		return 183
	elif city == 'Tampa':
		return 220
	elif city == 'Pittsburgh':
		return 222
	elif city	== 'Los Angeles':
		return 475

def rental_car_cost(days):
	car_rate = 40
	total_cost = car_rate * days
	if days >= 7:
		total_cost -= 50
	elif days >= 3:
		total_cost -= 20
	return total_cost


def trip_ride(city, days):
	return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city)  

print(trip_ride('Los Angeles' , 7))