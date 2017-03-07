'''
Douglas Huynh

Solve common algorithms using several data structures.

Mainly used to prepare for interviews.

'''


from collections import defaultdict

import unittest

############### Strings ###############

def isUnique_length(string):
	# O(N) time, O(N) space
	if string == None:
		return False

	return len(string) == len(set(string))


def isUnique_set(string):
	# O(N) time, O(N) space
	if string == None:
		return False

	characters = set()

	for char in string:
		if char in characters:
			return False
		else:
			characters.add(char)

	return True


def isUnique_bruteForce(string):
	# O(N^2) time, O(1) space
	if string == None:
		return False

	for i in range(0, len(string)):
		for j in range(i + 1, len(string)):
			if string[i] == string[j]:
				return False

	return True


def isPermutation_sorted(str1, str2):
	# O(n log n)
	if str1 == None or str2 == None:
		return False

	return sorted(str1) == sorted(str2)


def isPermutation_dict(str1, str2):
	# O(N)
	if str1 == None or str2 == None:
		return False

	if len(str1) != len(str2):
		return False

	str_dict1 = defaultdict(int)
	str_dict2 = defaultdict(int)

	for char in str1:
		str_dict1[char] += 1

	for char in str2:
		str_dict2[char] += 1

	return str_dict1 == str_dict2


def is_substring(s1, s2):
	return s1 in s2


def isRotation_substr(s1, s2):
	if s1 == None or s2 == None:
		return False

	if len(s1) != len(s2):
		return False

	return is_substring(s1, s2 + s2)


def reverseString_index1(string):

	string = list(string)

	if string == None or not string:
		return string

	size = len(string)

	for i in range(size // 2):
		string[i], string[size - 1 - i] = string[size - 1 - i], string[i]

	return ''.join(string)


def reverseString_index2(string):
	str_list = []
	index = len(string) - 1

	while index >= 0:
		str_list.append(string[index])
		index -= 1

	return ''.join(str_list)


def reverseString_r(string):

	if string == "":
		return string

	else:
		return reverseString_r(string[1:]) + string[0]


def firstNonRepeatingCharacter(string):
	order, counts = [], dict()

	for char in string:
		if char in counts:
			counts[char] += 1
		else:
			counts[char] = 1
			order.append(char)

	for char in order:
		if counts[char] == 1:
			return char

	return None



############### Arrays ###############

def twoNumSumArray(array, two_sum):
	left = 0
	right = len(array) - 1

	while left < right:
		if array[left] + array[right] == two_sum:
			return 1
		elif array[left] + array[right] < two_sum:
			left += 1
		else:
			right -= 1

	return 0


def maxSubArray(array):
	# Kadane's Algorithm
	# O(N)

	max_end = max_so_far = 0

	for element in array:
		max_end = max(0, max_end + element)
		max_so_far = max(max_so_far, max_end)

	return max_so_far


############### Linked Lists ###############

class LN(object):

	def __init__(self, value, next=None):
		self.value = value
		self.next = next

class LinkedList(object):

	def __init__(self, head=None):
		self.head = head

	def insertFront(self, value):
		new_node = LN(value)
		new_node.next = self.head
		self.head = new_node

	def printList(self):
		current = self.head
		while current is not None:
			print current.value
			current = current.next

	def size(self):
		current = self.head
		count = 0
		while current is not None:
			count += 1
			current = current.next

		return count

	def __len__(self):
		return self.size()

	def removeDups(self):
		# O(N), O(N)
		if self.head is None:
			return

		current = self.head
		seen = set()

		while current:
			if current.value not in seen:
				seen.add(current.value)
				prev = current
				current = current.next
			else:
				prev.next = current.next
				current = current.next

	def removeDups_SinglePointer(self):
		# O(N), O(N)
		if self.head is None:
			return

		current = self.head
		seen = set({current.value})

		while current.next is not None:

			if current.next.value in seen:
				current.next = current.next.next
			else:
				seen.add(current.next.value)
				current = current.next

	def removeDups_inPlace(self):
		# O(N^2), O(1) space
		if self.head is None:
			return

		current = self.head

		while current is not None:
			runner = current
			while runner.next is not None:
				if runner.next.value == current.value:
					runner.next = runner.next.next
				else:
					runner = runner.next

			current = current.next

	def kthToLastElement(self, k):
		# Assuming k = 1 means first to last place -> last place
		# k = 2, second to last place		

		if self.head is None:
			return None

		count = self.size() - k
		current = self.head

		while count > 0:
			count -= 1
			current = current.next

		return current.value

	def delete(self, value):
		current = self.head

		while current is not None:
			if current.value == value:
				self.deleteNode(current)

			current = current.next

	def deleteNode(self, node):
		if node is None:
			return None

		if node.next is None:
			node.value = None
		else:
			node.value = node.next.value
			node.next = node.next.next

	def reverse_list(self):
		reversed_ll = LinkedList()
		current = self.head

		while current is not None:
			reversed_ll.insertFront(current.value)
			current = current.next

		return reversed_ll

	def reverse(self):
		current = self.head
		prev = None

		while current is not None:
			next = current.next
			current.next = prev
			prev = current
			current = next

		self.head = prev


############### Stacks and Queues ###############

class LinkedStack(object):

	def __init__(self, top=None):
		self.top = top

	def push(self, value):
		self.top = LN(value, self.top)

	def pop(self):
		if self.top is None:
			return None

		value = self.top.value
		self.top = self.top.next
		return value

	def peek(self):
		return self.top.data if self.top is not None else None

	def isEmpty(self):
		return self.peek() is None


class LinkedQueue(object):

	def __init__(self):
		self.head = None
		self.tail = None

	def enqueue(self, item):
		node = LN(item)
		if self.head is None and self.tail is None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node

	def dequeue(self):
		if self.head is None and self.tail is None:
			return None

		value = self.head.value
		if self.head == self.tail:
			self.head = None
			self.tail = None
		else:
			self.head = self.head.next

		return value


############### Trees ###############

# Depth First Traversal (Preorder, Inorder, Postorder)

def preorderTraversal(root):
	if root:
		print root.data
		preorder(root.left)
		preorder(root.right)

def inorderTraversal(root):
	if root:
		inorder(root.left)
		print root.data
		inorder(root.right)

def postorderTraversal(root):
	if root:
		postorder(root.left)
		postorder(root.right)
		print root.data


def breadthFirstSearch_Tree(root):
	if root is None:
		return None

	queue = LinkedQueue()
	queue.enqueue(root)

	while queue:
		node = queue.dequeue()
		print node.value
		if node.left is not None:
			queue.enqueue(node.left)
		if node.right is not None:
			queue.enqueue(node.right)


def height(atree):
	if atree is None:
		return 0
	return 1 + max(height(atree.left), height(atree.right))


########### Sorting Algorithms ###########

def mergeSort(array):
	# Worst case O(N^2)
	# Avg case: O(N log N)
	result = []

	if len(array) < 2:
		return array

	mid = int(len(array) / 2)

	left = mergeSort(array[:mid])
	right = mergeSort(array[mid:])
	i, j = 0, 0

	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1

	result += left[i:]
	result += right[j:]
	return result


def selectionSort(array):
	# O(n^2)
	if array is None or len(array) < 2:
		return None

	for i in range(len(array) - 1):
		min_index = i
		for j in range(i + 1, len(array)):
			if array[j] < array[min_index]:
				min_index = j
		array[i], array[min_index] = array[min_index], array[i]

	return array


################## UNIT TESTS ##################

class TestStringAndArrays(unittest.TestCase):

	def test_IsUnique(self):
		self.assertTrue(isUnique_length('douglas'))
		self.assertFalse(isUnique_length('boo'))

	def test_IsPermutation(self):
		self.assertTrue(isPermutation_sorted('douglas', 'saldoug'))
		self.assertFalse(isPermutation_sorted('douglas', 'djflksdjf'))

	def test_reverse_index1(self):
		self.assertEqual(reverseString_index1('douglas'), 'salguod')

	def test_reverseString_index2(self):
		self.assertEqual(reverseString_index1('douglas'), 'salguod')

	def test_reverseString_r(self):
		self.assertEqual(reverseString_r('douglas'), 'salguod')


class TestSorting(unittest.TestCase):

	def setUp(self):
		self.temp = [4,3,6,8,1,9,10,2]

	def test_MergeSort(self):
		self.assertEqual(mergeSort(self.temp), [1,2,3,4,6,8,9,10])

	def test_SelectionSort(self):
		self.assertEqual(selectionSort(self.temp), [1,2,3,4,6,8,9,10])


if __name__ == '__main__':
	unittest.main()