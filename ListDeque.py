'''
Douglas Huynh

Implementation of ADT: Deque

Addition and removal of elements from either
front or rear.

'''

class Deque(object):

	def __init__(self):
		self.items = []

	def addFront(self, item):
		self.items.insert(0, item)

	def addRear(self, item):
		self.items.append(item)

	def removeFront(self):
		return self.items.pop(0)

	def removeRear(self):
		return self.items.pop()

	def isEmpty(self):
		return len(self.items) == 0

	def size(self):
		return len(self.items)

	def __str__(self):
		string = "["
		string += ",".join([str(elem) for elem in self.items])
		string += "]:rear"
		return string


def palindrome(string):
	'''Test if string is the same forwards and backwards using Deque'''
	deque = Deque()

	for i in string:
		deque.addRear(i)

	isPalindrome = True

	while deque.size() > 1 and isPalindrome:
		if deque.removeFront() != deque.removeRear():
			return False

	return isPalindrome

if __name__ == "__main__":

	d = Deque()
	d.addRear(2)
	d.addRear(3)
	d.addFront(1)
	assert(d.size() == 3)
	assert(d.isEmpty() == False)
	assert(palindrome("madam") == True)
	assert(palindrome("douglas") == False)