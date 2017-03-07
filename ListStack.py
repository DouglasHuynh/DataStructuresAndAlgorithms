'''
Douglas Huynh

Implementation of ADT: Stack

Addition and removal of elements from only top

'''

class Stack:
	def __init__(self):
		self.stack = []
		self.size = 0

	def isEmpty(self):
		return self.size == 0

	def push(self, item):
		self.stack.append(item)
		self.size += 1

	def pop(self):
		if self.isEmpty():
			raise Exception("No elements in Stack.")

		item = self.stack.pop()
		self.size -= 1
		return item

	def peek(self):
		if self.isEmpty():
			raise Exception("No elements in Stack.")

		return self._stack[-1]

	def size(self):
		return self.size

	def contains(self, item):
		return item in self._stack

	def __str__(self):
		string = "Stack["
		string += ",".join([str(elem) for elem in self.stack])
		string += "]:top"
		return string


def reverseString(string):
	'''Reverse a string using a Stack'''

	stack, reversed_string = Stack(), ""

	for index in range(len(string)):
		stack.push(string[index])

	for index in range(len(string)):
		reversed_string += stack.pop()

	return reversed_string


def main():
	stack = Stack()
	stack.push(4)
	stack.push(3)
	stack.push(1)
	stack.pop()
	stack.push(2)
	stack.push(5)
	print stack.contains(4)
	print stack
	print stack.peek()

	assert reverseString("reverse") == "esrever"
	assert reverseString("douglas") == "salguod"

if __name__ == "__main__":
	main()