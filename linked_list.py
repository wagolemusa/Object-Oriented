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
		"""
		Method insert to the node.

		"""
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			return 
		last_node = self.head
		while last_node.next:
			last_node = last_node.next
		last_node.next = new_node

	def prepend(self, data):
		"""
		Method Add Data on Top of a Node
		"""
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

	def delete_node(self, key):
		"""
		Method delete a node

		"""
		cur_node = self.head
		if cur_node and cur_node.data == key:
			self.head = cur_node.next
			cur_node = None
			return
		prev = None
		while cur_node and cur_node.data != key:
			prev = cur_node
			cur_node = cur_node.next
		if cur_node is None:
			return
		prev.next = cur_node.next
		cur_node = None

	def delete_node_at_pos(self, pos):
		"""
		Method Delete a Node in a postion

		"""
		cur_node = self.head
		if pos == 0:
			self.head = cur_node.next
			cur_node = None
			return 

		prev = None
		count = 1
		while cur_node and count != pos:

			prev = cur_node
			cur_node = cur_node.next
			count += 1

		if cur_node is None:
			return

		prev.next = cur_node.next
		cur_node = None


Llist = LinkedList()
Llist.append("A")
Llist.append("B")
Llist.append("C")
Llist.append("D")
# Llist.prepend("OL")
# It insert into after B
Llist.delete_node("B")
Llist.insert_after_node(Llist.head.next, "E")
Llist.insert_after_node(Llist.head.next, "P")
Llist.print_list()
