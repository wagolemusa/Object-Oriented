def make_greeting(title, name, surname, formal=True, time=None):
	if formal:
		fullname = "%s %s" %(title, surname)
	else:
		fullname = name
	if time is None:
		greeting = "Hello"
	else:
		greeting = "Good %s" % time

	return "%s, %s!" %(greeting, fullname)

print(make_greeting("MR", "john", "Smith"))
print(make_greeting("MR", "john", "Smith", False))
print(make_greeting("MR", "john", "Smith",False, "evening"))