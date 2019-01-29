import math

ADD, SUB, MUL, DIV = range(4)

def calculator(operation=ADD, output_formal=float, *args):
	if not args:
		raise ValueError("At least one number must be entered.")
	result = args[0]

	for n in args[1:]:
		if operation == ADD:
			result += n
		elif operation == SUB:
			result -= n
		elif operation == MUL:
			result *=n 
		elif operation == DIV:
			result /=n
		else:
			raise ValueError("operation must be ADD, SUB, MUL, DIV")
		if output_formal == float:
			result = float(result)
		elif output_formal == int:
			result = math.round(result)
		else:
			raise ValueError("Format must be float or int.")
		return result

n = 4, 5.0
print(calculator(n))