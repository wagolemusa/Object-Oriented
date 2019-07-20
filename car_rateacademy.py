"""
Define a function called rental_car_cost with an argument called days

a) Calculate the cost of renting the car.
---Every day rent the car costs $40.
--- if you rent the car for 7 or more days, you get $50 off your total.
----Alternatively(elif), if rent the car for 3 or more days,
		you get $20 off your total

----- You connot get both od the above discounts
----- Return the cost.

"""

def rental_car_cost(days):
	car_rate = 40
	total_cost = car_rate * days
	if days >= 7:
		total_cost -= 50
	elif days >= 3:
		total_cost -= 20
	return total_cost

print(rental_car_cost(8))