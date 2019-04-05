"""
Threre are seating categories at stadium for a softball game
class A seats cost 2000ksh, Class B seats Cost 1500 shs
Class C cost 1000ksh.Write a program that ask how many tickes for class of seats
were sold, and display the amount of income generated from ticket
soles
"""
def calculateClassTickectSales( classATicketsBought ):
	classASales = classATicketsBought * 2000
	return classASales

def calculateClassTickectSales( classBTicketsBought ):
	classBSales = classBTicketsBought * 1500
	return classBSales

def calculateClassTickectSales( classCTicketsBought ):
	classCSales = classCTicketsBought * 1000
	return classCSales

def calculateTotalSale( SalesA, SalesB, SalesC):
	totalSales = SalesA + SalesB + SalesC
	return totalSales

def printSales( SalesA, SalesB, SalesC, totalSales ):
	print( 	"Class A Seats: KSH" + format(SalesA),\
					"Class C Seats: KSH" + format(SalesB),\
					"Class A Seats: KSH" + format(SalesC),\
					"Total sales:   KSH" + format(totalSales))


def main():
	ticketA = int( input("How many tuckets were bought "+\
															" for class A ?"))
	ticketB = int( input("How many tuckets were bought "+\
															" for class B ?"))
	ticketC = int( input("How many tuckets were bought "+\
															" for class C ?"))

	SalesA = calculateClassTickectSales (ticketA )
	SalesB = calculateClassTickectSales (ticketB )
	SalesC = calculateClassTickectSales (ticketC )

	totalSales =  calculateTotalSale(SalesA, SalesB, SalesC)

	printSales(SalesA, SalesB, SalesC, totalSales)
	
main()
