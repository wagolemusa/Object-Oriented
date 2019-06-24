# Restaurant bills
def tax(bill):
	""" Add 8% tax to a restaurant bill"""
	bill *= 1.08
	print "With tax %f" % bill
	return bill 

def tip(tips):
	""" Add 5% tips """
	tips *= 1.15
	print "with tips %f" %tips
	return tips 

meal_coat = 100

print(tax(meal_coat))
print(tip(meal_coat))