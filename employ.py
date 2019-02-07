import datetime

class Person:

	def __init__(self, name, sunname, birthdate, address, telephone, email):
		self.name = name
		self.sunname = sunname
		self.birthdate = birthdate
		self.address = address
		self.telephone = telephone
		self.email = email

	def age(self):
		today = datetime.date.today()
		age = today.year - self.birthdate.year

		if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
			age -= 1
		return age

person = Person(
	"jane",
	"Dee",
	datetime.date(1992,1,21),
	"Kisum streete",
	"55467677",
	"homie@gmail.com"
)

print(person.name)
print(person.email)
print(person.age())
