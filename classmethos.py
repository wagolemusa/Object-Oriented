
import datetime

class Employee:

	raise_amount = 1.04
	count = 0

	def __init__(self, fname, lname, pay):
		self.fname = fname
		self.lname = lname
		self.pay  = pay
		self.email = fname + '.' + lname + '@gmail.com'

		Employee.count += 1

	def fullname(self):
		return '{} {}'.format(self.fname, self.lname)

	def arise_pay(self):
		self.pay = int(self.pay * self.raise_amount)


	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount

	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True

my_date = datetime.date(2019,	9, 26)


emp_1 = Employee('Gorey', 'sherl', 5000)
emp_2 = Employee('Test', 'musa', 6000)



Employee.set_raise_amt(1.05)

print(Employee.is_workday(my_date))
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


emp_str_1 = 'john-Dee-70000'
emp_str_2 = 'Steve-Smith-3000'
emp_str_3 = 'jone-Doe-90000'

new_empl_1 = Employee.from_string(emp_str_1)

# print(new_empl_1)

# print(new_empy.email)
print(new_empl_1.pay)
print(new_empl_1.fullname())
