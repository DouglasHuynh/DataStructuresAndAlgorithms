'''
Douglas Huynh

Implementation of Data Structure: Binary Search Tree

'''

class TreeNode():

	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


class BinarySearchTree:

	def __init__(self, root=None):
		self.root = root

	def size(self):
		if self.root == None:
			return 0
		else:
			return 1 + size(self, self.root.left) + size(self, self.root.right)


	def add(self, value):
		if self.root == None:
			return TreeNode(value)

		if value < self.root.value:
			self.root.left = add(self, root.left, value)

		elif value > self.root.value:
			self.root.right = add(self, self.root.right, value)
		else:
			return self.root


if __name__ == "__main__":
	tree = BinarySearchTree()
	tree.add(1)
	tree.add(2)
	print tree.size()