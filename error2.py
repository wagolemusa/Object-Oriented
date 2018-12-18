try:
	dividend = int(input("please enter the dividend: "))
	divisor = int(input("Please the divisor: "))
	print("%d / %d = %f" %(dividend, divisor, dividend/divisor))
except(ValueError, ZeroDivisionError):
	print("Oops, something went wrog!")