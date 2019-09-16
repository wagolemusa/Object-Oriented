class Employee:

	def __init__(self, fname, lname, pay):

		self.fname = fname
		self.lname = lname
		self.pay = pay
		self.email = fname + '.' + lname  + '@refuge.com'

	def fullname(self):
		return '{} {}'.format(self.fname, self.lname)




emp_1 = Employee('Gorey', 'sherl', 5000)
emp_2 = Employee('Test', 'musa', 6000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())