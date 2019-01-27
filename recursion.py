# Write a recursive function which calculates the factorial of a given number. 
# Use exception handling to raise an appropriate exception if the input parameter is not a positive integer, 
# but allow the user to enter floats as long as they are whole numbers.

def factorial(n):
	ni = int(n)
	if ni != n or ni <= 0:
		raise ValueError("%s is not a postive integer." %n)
	if ni == 1:
		return 1
	return ni * factorial(ni - 1)

n = (4.9)
print(factorial(n))
