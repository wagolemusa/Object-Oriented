class Employee:

	num_of_emps = 0
	raise_amount = 1.04

	def __init__(self, fname, lname, pay):
		self.fname = fname
		self.lname = lname
		self.pay   = pay
		self.email = fname + '.' + lname

		# Counts employees
		Employee.num_of_emps += 1

	# It retusrns full names
	def fullname(self):
		return '{} {}'.format(self.fname, self.lname)

	# This raises the amount
	def aply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	# This Danda methed it was design for developers to understand
	def __repr__(self):
		return "Employee('{}', '{}','{}'".format(self.fname, self.lname, self.pay)

	# This Danda methed its was design to be for user
	def __str__(self):
		return '{} - {}'.format(self.fullname(), self.email)

	# This in bulit methed for additons
	def __add__(self, other):
		return self.pay + other.pay

emp_1 = Employee('Gorey', 'sherl', 5000)
emp_2 = Employee('Test', 'musa', 6000)

# print(emp_2.raise_amount)

# print(count)

print(emp_1 + emp_2)
print(repr(emp_1))
print(str(emp_1))