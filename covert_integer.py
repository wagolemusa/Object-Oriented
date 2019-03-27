"""
Use a stack data structure to covert integer values to  binary.

1. will devide 242 / 2  -> 0
121 / 2 = 60 - > 1
60 / 2 = 15 -> 	 0
15 / 2 = 7  ->   1
7 / 2  = 3  ->   1
3 / 2  = 1  ->   1
1 / 2  = 0  ->   1
"""

from stack import Stack

def dev_by_2(dec_num):
	s = Stack()
	while dec_num  > 0:
		# take the raminder of the devision
		reminder = dec_num % 2
		#  Pust the remainder in the satck
		s.push(reminder)
		# pass // to divide any number
		dec_num = dec_num // 2

		# We declare an empty string
	bin_num = ""
	# we check is the stack in empty
	while not s.is_empty():
		# it pops to the bin_num3
		bin_num += str(s.pop())

	return bin_num

print (dev_by_2(242))

