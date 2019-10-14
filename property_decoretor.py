class Employee:

	def __init__(self, fname, lname, pay):
		self.fname = fname
		self.lname = lname
		self.pay = pay

	@property
	def fullname(self):
		return '{} {}'.format(self.fname, self.lname)

	@property
	def email(self):
		return '{}.{}@gmail.com'.format(self.fname, self.lname)

	@fullname.setter
	def full(self, name):
		fname, lname = name.split(' ')
		self.fname = fname
		self.lname = lname

emp_1 = Employee('John', 'Smath', 6000)

emp_1.full = 'refuge wise'

print(emp_1.fname)

print(emp_1.fullname)
print(emp_1.email)

