from string import Template

class Mytemplate(Template):
	delimiter = '#'

def Main():
	cart = []
	cart.append(dict(item="Coke", price=7, qty=4))
	cart.append(dict(item = "posh", price = 32, qty= 5))
	cart.append(dict(item = "fish", price = 64, qty = 8))
	t = Mytemplate("#qty * #item = #price")

	total = 0
	print ("Cart:")

	for data in cart:
		print t.substitute(data)
		total += data["price"]
	print "Total:" + str(total)

if __name__ == '__main__':
	Main()