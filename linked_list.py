class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def print_list(self):
		cur_node = self.head
		while cur_node:
			print(cur_node.data)
			cur_node = cur_node.next

	def append(self, data):
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			return 
		last_node = self.head
		while last_node.next:
			last_node = last_node.next
		last_node.next = new_node

	def prepend(self, data):
		new_node = Node(data)

		new_node.next = self.head
		self.head = new_node


	def insert_after_node(self, prev_node, data):
		"""
		Method insert data to previous 
		"""
		if not prev_node:
			print("Previous node is not in a list")
		new_node = Node(data)
		new_node.next = prev_node.next
		prev_node.next = new_node



Llist = LinkedList()
Llist.append("A")
Llist.append("B")
Llist.append("C")
Llist.append("D")
# Llist.prepend("E")
# It insert into after B
Llist.insert_after_node(Llist.head.next, "E")
Llist.print_list()

