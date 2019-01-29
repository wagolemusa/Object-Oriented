import math
ADD, SUB, MUL, DIV = range(4)
def calculator(a, b, operation=ADD, output_format=float):
	if operation == ADD:
		result = a + b
	elif operation == SUB:
		result = a - b
	elif operation == MUL:
		result = a * b
	elif operation == DIV:
		result = a /b
	else:
		raise ValueError("operation must be ADD, SUB, MUL, DIV")
	if output_format == float:
		result = float(result)
	elif output_format == int:
		result = math.round(result)
	else:
		raise ValueError("Format must be float or integer.")
	return result
print(calculator(5.0, 7))
print(calculator(10, 5))