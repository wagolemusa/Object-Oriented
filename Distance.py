"""
-Distance Traveled 
the distance of a vehicle can be calculated as followers:
- distance = speed = time
For example if a train travel 40 miles per hour for three hours,
the distance traveled is 120 miles.
- write a program that ask the user for the spend of vehicle( in miles per hour)
and the number of hours it has traveled.
It should then use a loop to display
the distance the vehicle has traveled for each hour of that time period

what is the speed of the vehicle in nmp? 40	
How many hours has it travelled

hours    Distance Traveled
1	        40
2         80
3					120
"""
vehicleSpeed = float(input("What is spend vechicle:"))
timeTraveled = int(input("How many hours has it traveled"))

print("Hours", "Distance Traveled")
for currentHour in range(1, timeTraveled + 1):
	distanceTraveled = 	vehicleSpeed * currentHour

	print(currentHour, distanceTraveled)