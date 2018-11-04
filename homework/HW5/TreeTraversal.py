from enum import Enum
class Node2:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, val):
        if self.root:
            self.insert_recursion(val, self.root)
        else:
            self.root = Node2(val)          
            
    def insert_recursion(self, val, node):
        if val < node.val:
            if node.left:
                self.insert_recursion(val, node.left)
            else:
                node.left = Node2(val)
        else:
            if node.right:
                self.insert_recursion(val, node.right)
            else:
                node.right = Node2(val)
            
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
    
class DFSTraversal:
    def __init__(self, tree, traversalType):
        self.root = tree.root
        self.traversalType = traversalType
        self.nodes = []
        self.traverseAllNodes()
        self.index = 0
        
    def traverseAllNodes(self):
        if self.traversalType==DFSTraversalTypes.PREORDER:
            self.preOrder(self.root)
        if self.traversalType==DFSTraversalTypes.INORDER:
            self.inOrder(self.root)
        if self.traversalType==DFSTraversalTypes.POSTORDER:
            self.postOrder(self.root)
            
    def preOrder(self, node):
        if node:
            self.nodes.append(node.val)
            self.preOrder(node.left)
            self.preOrder(node.right)
        
    def inOrder(self, node):
        if node:
            self.inOrder(node.left)
            self.nodes.append(node.val)
            self.inOrder(node.right)

    def postOrder(self, node):
        if node:
            self.postOrder(node.left)
            self.postOrder(node.right)
            self.nodes.append(node.val)
        
        
    def changeTraversalType(self, traversalType):
        self.traversalType = traversalType
        self.nodes = []
        self.traverseAllNodes()
        self.index = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        try:
            node_val = self.nodes[self.index] 
        except IndexError:
            raise StopIteration() 
        self.index += 1
        return node_val