'''
Douglas Huynh

Implementation of ADT: Queue

Addition at rear and removal at front.

'''

class Queue:
	def __init__(self):
		self._queue = []
		self.size = 0

	def isEmpty(self):
		return self.size == 0

	def size(self):
		return self.size

	def front(self):
		if self.isEmpty():
			raise Exception("No elements in the queue")
		return self._queue[0]

	def rear(self):
		if self.isEmpty():
			raise Exception("No elements in the queue")
		return self._queue[-1]

	def enqueue(self, item):
		self._queue.append(item)
		self.size += 1

	def dequeue(self):
		if self.isEmpty():
			raise Exception("No elements in the queue")

		self.size -= 1
		return self._queue.pop(0)

	def contains(self, item):
		return item in self._queue

	def __str__(self):
		string = "Queue:["
		string += ",".join([str(elem) for elem in self._queue])
		string += "]:rear"
		return string


def main():
	queue = Queue()
	queue.enqueue(1)
	queue.enqueue(2)
	queue.enqueue(3)
	print queue
	queue.dequeue()
	print queue
	print queue.contains(2)
	print queue.front()
	print queue.rear()


if __name__ == "__main__":
	main()