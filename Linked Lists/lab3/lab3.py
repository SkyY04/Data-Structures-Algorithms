#
# Author: Saeha Yoon
# Student Number: 139277222
#
# Place the code for your lab 3 here.  Read the specs carefully.  
#
# To test, run the following command :
#     python test_lab3.py
#


class DoublyLinked:

	class Node:
		def __init__(self, data, next = None, prev = None):
			self.data = data
			self.next = next
			self.prev = prev

		# return data stored in the node
		def get_data(self):
			return self.data

		# return a reference to next node
		def get_next(self):
			return self.next

		# return a reference to previous node
		def get_previous(self):
			return self.prev

	def __init__(self, data = None):
		self.front = None
		self.back = None

	def get_front(self):
		return self.front

	def get_back(self):
		return self.back

	def push_front(self, data):
		new_node = self.Node(data, next=self.front)
		if self.front is not None:
			self.front.prev = new_node
		else:
			self.back = new_node
		self.front = new_node

	def push_back(self,data):
		new_node = self.Node(data, prev=self.back)
		if self.back is not None:
			self.back.next = new_node
		else:
			self.front = new_node
		self.back = new_node

	def pop_front(self):
		if self.front is None:
			raise IndexError('pop_front() used on empty list')
		data = self.front.data
		self.front = self.front.next
		if self.front is not None:
			self.front.prev = None
		else:
			self.back = None
		return data

	def pop_back(self):
		if self.back is None:
			raise IndexError('pop_back() used on empty list')
		data = self.back.data
		self.back = self.back.prev
		if self.back is not None:
			self.back.next = None
		else:
			self.front = None
		return data


class Sentinel:

	class Node:
		def __init__(self, data, next = None, prev = None):
			self.data = data
			self.next = next
			self.prev = prev

		# return data stored in the node
		def get_data(self):
			return self.data

		# return a reference to next node
		def get_next(self):
			return self.next

		# return a reference to previous node
		def get_previous(self):
			return self.prev

	def __init__(self, data = None):
		self.front = self.Node(None)
		self.back = self.Node(None)
		self.front.next = self.back
		self.back.prev = self.front

	# return a reference to the first data node
	# If the list is empty, return None
	def get_front(self):
		return self.front.next if self.front.next != self.back else None

	# return a reference to the last data node
	# If the list is empty, return None
	def get_back(self):
		return self.back.prev if self.back.prev != self.front else None

	# add data to the front of the list
	def push_front(self, data):
		new_node = self.Node(data, next=self.front.next, prev=self.front)
		self.front.next.prev = new_node
		self.front.next = new_node

	# add data to the back of the list
	def push_back(self,data):
		new_node = self.Node(data, next=self.back, prev=self.back.prev)
		self.back.prev.next = new_node
		self.back.prev = new_node

	# remove the first data from the list
	def pop_front(self):
		if self.front.next == self.back:
			raise IndexError('pop_front() used on empty list')
		data = self.front.next.data
		self.front.next = self.front.next.next
		self.front.next.prev = self.front
		return data

	# remove the last data from the list
	def pop_back(self):
		if self.back.prev == self.front:
			raise IndexError('pop_back() used on empty list')
		data = self.back.prev.data
		self.back.prev = self.back.prev.prev
		self.back.prev.next = self.back
		return data






