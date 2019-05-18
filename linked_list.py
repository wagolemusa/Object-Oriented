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

	def len_iterative(self):
		"""
		Count Nodes
		"""
		count = 0
		cur_node = self.head

		while cur_node:
			count += 1
			cur_node = cur_node.next
		return count

	def len_recursive(self, node):
		"""
		Length of Node
		"""
		if node is None:
			return 0
		return 1 + self.len_recursive(node.next)


	def swap_nodes(self, key_1, key_2):
		"""
		Swap to the next Node
		"""
		if key_1 == key_2:
			return

		prev_1 = None
		curr_1 = self.head
		while curr_1 and curr_1.data != key_1:
			prev_1 = curr_1
			curr_1 = curr_1.next

		prev_2 = None
		curr_2 = self.head
		while curr_2 and curr_2.data != key_2:
			prev_2 = curr_2
			curr_2 = curr_2.next

		if not curr_1 or not curr_2:
			return

		if prev_1:
			prev_1.next = curr_2
		else:
			self.head = curr_2
		if prev_2:
			prev_2.next = curr_1
		else:
			self.head = curr_1

		curr_1.next, curr_2.next = curr_2.next, curr_1.next

	def print_helper(self, node, name):
		if node is None:
			print(name + ": None")
		else:
			print(name + ":" + node.data)

	def reverse_iterative(self):
		"""
		A -> B -> C -> D -> 0
		D -> C -> B -> A -> 0
		A -> B -> C -> D <- 0

		"""
		prev = None
		cur = self.head
		while cur:
			nxt = cur.next
			cur.next = prev
			self.print_helper(prev, "PREV")
			self.print_helper(cur, "CUR")
			self.print_helper(nxt, "NXT")
			print("\n")
			prev = cur
			cur = nxt
		self.head = prev
	
	def reverse_recursive(self):

		def _reverse_recursive(cur, prev):
			if not cur:
				return prev
			nxt = cur.next
			cur.next = prev
			prev = cur
			cur = nxt
			return _reverse_recursive(cur, prev)
		self.head = _reverse_recursive(cur=self.head, prev=None) 


	def merge_sorted(self, Llist):
		"""
		This function sorts the  different lists
		eg p = 1,5,7,9,10
			q = 2,3,4,6,8
		To  s = 1,2,3,4,5,6,7,8,9,10

		"""
		p = self.head
		q = Llist.head
		s = None 
		if not p:
			return q
		if not q:
			return p
		if p and q:
			if p.data <= q.data:
				s = p
				p = s.next
			else:
				s = q
				q = s.next
			new_head = s

		while p and q:
			if p.data <= q.data:
				s.next = p
				s = p
				p = s.next
			else:
				s.next = q
				s = q
				q = s.next
		if not p:
			s.next = q
		if not q:
			s.next = p
		return new_head

	def remove_duplication(self):
		"""
		Origin List
		1 -> 6 -> 1 -> 4 -> 2 -> 2 ->4
		Remove duplicates
		1 -> 6 -> 4 -> 2
		"""
		cur = self.head
		prev = None
		dup_values = dict()
		while cur:
			if cur.data in dup_values:
				#Reveme
				prev.next = cur.next
				cur = None 
			else:
				# Have not encountered element before
				dup_values[cur.data] = 1
				prev = cur
			cur = prev.next

# Llist_1 = LinkedList()
# Llist_2 = LinkedList()

# Llist_1.append(1)
# Llist_1.append(5)
# Llist_1.append(7)
# Llist_1.append(9)
# Llist_1.append(10)

# Llist_2.append(2)
# Llist_2.append(3)
# Llist_2.append(4)
# Llist_2.append(6)
# Llist_2.append(8)

Llist = LinkedList()
Llist.append(1)
Llist.append(6)
Llist.append(1)
Llist.append(4)
Llist.append(2)
Llist.append(4)
Llist.remove_duplication()
Llist.print_list()


# Llist_1.merge_sorted(Llist_2)
# Llist_1.print_list()
# print("\n")
# Llist_2.print_list()

Llist = LinkedList()
Llist.append("A")
Llist.append("B")
Llist.append("C")
Llist.append("D")
Llist.reverse_iterative()
Llist.reverse_recursive()
# Llist.prepend("OL")
# It insert into after B
# Llist.delete_node("B")
# Llist.insert_after_node(Llist.head.next, "E")
# Llist.insert_after_node(Llist.head.next, "P")
Llist.swap_nodes("A", "C")

Llist.print_list()
print(Llist.len_iterative())
print(Llist.len_recursive(Llist.head))

