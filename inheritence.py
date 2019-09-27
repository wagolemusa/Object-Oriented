class Employee:

	raise_amount = 1.04
	def __init__(self, fname, lname, pay):

		self.fname = fname
		self.lname = lname
		self.pay = pay
		self.email = fname + '.' + lname  + '@refuge.com'

	def fullname(self):
		return '{} {}'.format(self.fname, self.lname)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
	raise_amount = 1.10 

	def __init__(self, fname, lname, pay, prog_lang):
		super().__init__(fname, lname, pay)
		self.prog_lang = prog_lang

class Manager(Employee):
	def __init__(self, fname, lname, pay, employees=None):
		super().__init__(fname, lname, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_empl(self):
		for emp in self.employees:
			print('----->', emp.fullname()) 


dev_1 = Developer('Gorey', 'sherl', 50000, 'python')
dev_2 = Developer('Test', 'musa', 60000, 'java')

man_1 = Manager('Sue', 'smath', 90000,[dev_1])

print(man_1.email)
	man_1.add_emp(dev_1)
man_1.print_empl()



# print(dev_1.email)
# dev_1.apply_raise()
print(dev_1.prog_lang)

# print(emp_1.email)
# print(emp_2.email)

# print(emp_1.fullname())	