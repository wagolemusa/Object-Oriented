"""
Write a program that will ask a user to enter the amount of purchase
the program should then compute the state and county sales tax.
Assume the state sales tax is 5 percent and the county sales 
is 2.5 percent.
The program should display the amount of purchase, the state sales tax,
The county sales tax, the total sales tax, and the total of the sale,
(Which is the sum of the amount of purchase plus the tatol sales tax)

# Hint Use value of 0.025 to represent 2.5 percent.
and 0.05 to represent 5 percent
"""

AmountSalesUser = float(input("Enter the amount of purchase"))

stateTax = 0.05 * AmountSalesUser
countyTax = 0.025 * AmountSalesUser

totalTax = stateTax + countyTax

totalSales = AmountSalesUser + totalTax


print ("Amount of purchase $ "+ format( AmountSalesUser, ",.2f"), \
				"Sales Tax $"+ format(stateTax, ",.2f"), \
				"County Tax $" + format(countyTax, ",.2f"), \
				"Total Tax $" + format(totalTax, ",.2f"),\
				"Total Sales $" + format(totalSales, ",.2f"), sep = "\n")