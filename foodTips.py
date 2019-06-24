"""
Write a program that calculates the total amount of a meal
purchesed at a 	restaurant. the program should be ask a user 
to enter the charge for the food. and the calculate the amount of
a 18 percent tip and 7 percent sales tax.
display each these amount and the total.
"""


foodCharge = float(input(" Please enter the charge" ))
tip = 0.18 * foodCharge
salesTax = 0.07 * foodCharge

total = foodCharge + tip + salesTax

print (" food charge: $" + format( foodCharge,",.2f"),\
				"Tip $" + format ( tip, ",.2f"),\
				"Sales Tax" + format ( salesTax, ",.2f"),\
				"Total" + format (total, ",.2f"))
# , sep = "\n"