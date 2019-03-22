
# Stack Data Structure
class Stack():
	def __init__(self):
		self.items = []

	# this function add to the items list
	def push(self, item):
		self.items.append(item)

	# this function return the top element on the stack
	def pop(self):
		return self.items.pop()

	# This function will return if the list is empty
	def is_empty(self):
		return self.items == []

	def peek(self):
		if not self.is_empty():
			return self.items[-1]
		else:
			return False

	# This function return the stack in the items list
	def get_stack(self):
		return self.items

s = Stack()
s.push('A') #added 'A' to list
s.push('B') #added 'B' to a list
print(s.get_stack()) # We printed it out
s.push('C') # We added 'C' on top of alist 
print(s.get_stack()) # We printed it out
s.pop() # We poped or removed 'C' on top of a list
s.push('D')
s.push('T')
print(s.get_stack()) # Then We printed it again 

print(s.is_empty()) # This should return false because the list is not empty

print(s.peek())