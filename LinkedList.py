'''
Douglas Huynh

Implementation of Linked List

Collection of nodes, each node contains
reference to next node or null.

'''

class Node(object):

	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setNext(self, newNext):
		self.next = newNext


class LinkedList(object):

	def __init__(self, head=None):
		self.head = head


	def add(self, data):
		new_node = Node(data)
		new_node.setNext(self.head)
		self.head = new_node

	def search(self, data):
		current = self.head
		while current:
			if current.getData() == data:
				break
			else:
				current = current.getNext()

		if current == None:
			return ValueError("Data not in list")

		return current

	def size(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.getNext()

		return count

	def contains(self, data):
		current = self.head
		while current:
			if current.getData() == data:
				return True
			else:
				current = current.getNext()

		return False

	def delete(self, data):
		current = self.head
		previous = None
		while current:
			if current.getData() == data:
				if previous is not None:
					previous.next = current.next
				else:
					self.head = current.next

			previous = current
			current = current.next

	def toString(self):
		current = self.head
		print "LinkedList[",
		while current:
			print current.getData(), 
			current = current.getNext()
		print "]"


if __name__ == "__main__":
	test_list = LinkedList()
	test_list.add(1)
	test_list.add(2)
	test_list.add(4)
	test_list.toString()
	print test_list.search(3)
	print test_list.contains(3)
	print test_list.contains(1)
	test_list.delete(2)
	test_list.toString
	print test_list.size()