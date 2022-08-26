class Node:
    def __init__(self, value):
        self.l = None
        self.r = None 
        self.v = value 

class BinaryTree: 
    def __init__(self) -> None: 
        self.root = None 
        self.size = 0 

    def add(self, value): 
        if self.root is None:
            self.root = Node(value) 
        else: 
            self._add(value, self.root)
            
    def _add(self, value, node):
        if value < node.v: 
            if node.l is not None:
                self._add(value, node.l)
            else: 
                node.l = Node(value)
        else: 
            if node.r is not None:
                self._add(value, node.r)
            else: 
                node.r = Node(value)

    def find(self, value): 
        if self.root is not None:
            return self._find(value, self.root)
        else: 
            return None
    
    def _find(self, target, node: Node) -> Node: 
        # base case by returning the value when found 
        if target == node.v: 
            return node.v
        # move left if target is smaller than the current 
        elif(target < node.v and node.l is not None):
            return self._find(target, node.l)
       # move right if target is bigger than the current 
        elif(target > node.v and node.r is not None):
            return self._find(target, node.r)

    def invertTree(self):
        if self.root is None:
            return None
        else: 
            self._invertTree(self.root)        

    def _invertTree(self, node: Node) -> Node:
        # swap sides 
        if node is not None:
            tmp = node.l
            node.l = node.r
            node.r = tmp

            self._invertTree(node.l)
            self._invertTree(node.r)
        return node        
    
    def printTree(self, type):
        if self.root is not None: 
            if type == 'in-order':
                self._printInOrder(self.root)
            elif type == 'pre-order':
                self._printPreOrder(self.root)
            elif type == 'post-order': 
                self._printPostOrder(self.root)        

    def _printInOrder(self, node): 
        if node is not None: 
            self._printInOrder(node.l)
            print(str(node.v) + '->') 
            self._printInOrder(node.r)

    def _printPreOrder(self, node): 
        if node is not None: 
            print(str(node.v) + '->') 
            self._printPreOrder(node.l)
            self._printPreOrder(node.r)

    def _printPostOrder(self, node): 
        if node is not None: 
            self._printPreOrder(node.l)
            self._printPreOrder(node.r)
            print(str(node.v) + '->') 


tree = BinaryTree()
tree.add(1)
tree.add(2)
tree.add(3)
tree.add(4)
tree.add(5)

# print(tree.find(3))
# print(tree.find(1))

# tree.printTree('in-order')
# tree.invertTree() 
# tree.printTree('in-order')

tree.printTree('post-order')
tree.printTree('in-order')