try:
	age = int(input("Please	enter your age:"))
	print("I see is your are %d years old." %age)
except ValueError:
	print("Hey,that was'nt a number!")