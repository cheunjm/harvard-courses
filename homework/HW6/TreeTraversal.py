from enum import Enum

class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class BinaryTree:
	def __init__(self):
		self.root = None

	# 10 pts
	def insert(self, val):
		if self.root:
			self.insert_recursion(val, self.root)
		else:
			self.root = Node(val)

	def insert_recursion(self, val, node):
		if val < node.val:
			if node.left:
				self.insert_recursion(val, node.left)
			else:
				node.left = Node(val)
		else:
			if node.right:
				self.insert_recursion(val, node.right)
			else:
				node.right = Node(val)

	# 10 pts
	def getValues(self, depth):
		prev = [self.root]
		d = 0
		while d < depth:
			curr = []
			for i in prev:
				if i:
					curr.append(i.left)
					curr.append(i.right)
				else:
					curr.append(None)
					curr.append(None)
			d +=1
			if all(curr) is None:
				raise ValueError("Invalid depth.")
			prev = curr
		ans = []
		for j in prev:
			if j:
				ans.append(j.val)
			else:
				ans.append(None)
		return ans

	# 10 pts
	def remove(self, val):
		curr = self.root
		left = True
		prev = None
		while val != curr.val:
			prev = curr
			if val < curr.val:
				curr = curr.left
			else:
				left = False
				curr = curr.right
		if (not curr.left) and (not curr.right):
			if left:
				prev.left = None
			else:
				prev.right = None
		elif curr.left and (not curr.right):
			if left:
				prev.left = curr.left
			else:
				prev.right = curr.left
		elif (not curr.left) and curr.right:
			if left:
				prev.left = curr.right
			else:
				prev.right = curr.right
		else:
			prev = curr
			curr = curr.left
			temp = None
			while curr.right:
				temp = curr
				curr = curr.right
			prev.val = curr.val
			if temp:
				temp.right = None

class DFSTraversalTypes(Enum):
	PREORDER = 1
	INORDER = 2
	POSTORDER = 3

class DFSTraversal():
	def __init__(self, tree, traversalType):
		self.index = 0
		self.root = tree
		self.traversalType = traversalType
		self.nodes = []
		self.traverse()

	def traverse(self):
		if self.traversalType == DFSTraversalTypes.PREORDER:
			self.preorder(self.root)
		elif self.traversalType == DFSTraversalTypes.INORDER:
			self.inorder(self.root)
		elif self.traversalType == DFSTraversalTypes.POSTORDER:
			self.postorder(self.root)

	def changeTraversalType(self, traversalType):
		self.index = 0
		self.traversalType = traversalType
		self.nodes = []
		self.traverse()

	def __iter__(self):
		return self

	def __next__(self):
		try:
			node = self.nodes[self.index]
		except IndexError:
			raise StopIteration()
		self.index += 1
		return node

	def inorder(self, bt):
		#Traverse left-subtree, then current root, then right sub tree
		if bt is not None:
			self.inorder(bt.left)
			self.nodes.append(bt)
			self.inorder(bt.right)

	def preorder(self, bt):
		# Current root, then traverse left subtree, then traverse right subtree
		if bt is not None:
			self.nodes.append(bt)
			self.preorder(bt.left)
			self.preorder(bt.right)

	def postorder(self, bt):
		# Traverse left subtree, then traverse right subtree, and then current root
		if bt is not None:
			self.postorder(bt.left)
			self.postorder(bt.right)
			self.nodes.append(bt)