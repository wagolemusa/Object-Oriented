#import the csv module so we can write data to csv
import csv
# imports the random module so we can generate a random number
import random 

def searchbookinggref():
	data = []
	with open("cinama.csv") as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			data.append(row)
	print (data)

	look = input("Please enter a file name: ")

	col4 = [x[2] for x in data]
	print(col4)
	if look in col4:
	# searches through column 4 to find all instances of the films name
	# if it finds a macth the index (row) number of the natch is noted as 'k'
	#data [k] in range prints all the information in row
		for k in range (0, len(col4)):
			if col4[k] == look:
				# print("test")
				print(data[k])
				# results.append(k)
	else:
		print("No film with that name")


def addbooking():
	#makes a 2D array called bookings. This is where the collected data.
	# is going to before written to the csv file
	bookings = []

	data = []
	with open("cinama.csv") as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			data.append(row)
	# creates a random number between 0 and 100 for the booking ref
	bookingref = random.randint(1, 1000)
	#conv this number from integer to string as integers con't be written to a csv file
	bookingref = str(bookingref)
	coll = [x[0] for x in data]
	# just test if its looking for booking numbers
	print(coll)
	if bookingref in coll:
		bookingref = int(bookingref)
		# code to make a new booking ref
		bookingref2 = random.randint(1,1000)
		newbookingref = bookingref * bookingref2
		newbookingref = str(newbookingref)
		bookings.append(newbookingref)

		print("The booking ref is", newbookingref)
		# asks then to enter details
		surname = input("please enter your surname")
		forename = input("Please enter your forename")
		film = input("Please enter the film you want see")
		day = input("What day of the week do you want see the film?")
		# adds these details to the 2D array called 'bookings'
		#addpend means add
		bookings.append(bookingref)
		bookings.append(surname)
		bookings.append(forename)
		bookings.append(film)
		bookings.append(day)
		# takes all the informaion in the 2D array 'bookings' and writes it
		#to the csv file colled 'cinema.csv'
		with open("cinama.csv", "a", newline='') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerow(bookings)

	else:
		print("The booking ref is", bookingref)
		# asks then to enter details
		surname = input("please enter your surname")
		forename = input("Please enter your forename")
		film = input("Please enter the film you want see")
		day = input("What day of the week do you want see the film?")
		# adds these details to the 2D array called 'bookings'
		#addpend means add
		bookings.append(bookingref)
		bookings.append(surname)
		bookings.append(forename)
		bookings.append(film)
		bookings.append(day)
		# takes all the informaion in the 2D array 'bookings' and writes it
		#to the csv file colled 'cinema.csv'
		with open("cinama.csv", "a", newline='') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerow(bookings)

# Menu system
print ("Welcome to the soloon booking system")
print ("Select an option to contince")

print ("Press 1 to book the service")
print ("Press 2 to search service")


choice = input("Please select an option abave")

if choice == "1":
	addbooking()

elif choice == "2":
	searchbookinggref()
	# print("test print statement to see if choice 2 works")
else:
	print("Invalid entry")