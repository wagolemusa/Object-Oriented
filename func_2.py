
    # Rewrite the hypotenuse function from exercise 2 so that it 
    # returns a value instead of printing it. Add exception handling so 
    # that the function returns None if it is called with parameters of the wrong type.
    # Call the function with two numbers, and print the result.
    # Call the function with two strings, and print the result.
    # Call the function with a number and a string, and print the result.
import math
def hypotenuse(a, b):
	try:
		return math.sqrt(a**2 + b**2)
	except TypeError:
		return None

print(hypotenuse(34, 6))
print(hypotenuse("8", "5"))
print(hypotenuse(34, "5"))


