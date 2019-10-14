from string import Template

def Main():
	cart = []
	cart.append(dict(item = "Cups", price = 200, qty = 2))
	cart.append(dict(item = "shoes", price = 300, qty = 3))
	cart.append(dict(item = "sharts", price = 500, qty = 1))

	t = Template("$qty * $item = $price")

	total = 0
	print "Cart"
	for data in cart:
		print t.substitute(data)
		total += data["price"]
	print "Total" + str(total)



if __name__ == "__main__":
	Main()