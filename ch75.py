class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

class Node:
    def __init__(self, val):
        self.data = val
        self.left, self.right = None, None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def add(self, leftChild, rightChild):
        if leftChild:
            self.leftChild = leftChild
        if rightChild:
            self.rightChild = rightChild

    def print(self):
        self._print_tree_structure(self, 0)

    def _print_tree_structure(self, root, level):
        if root is not None:
            self._print_tree_structure(root.rightChild, level + 1)
            print('     ' * level , str(root.data))
            self._print_tree_structure(root.leftChild, level + 1)

    def infix(self):
        if self.data is not None:
            if self.leftChild is not None or self.rightChild is not None:
                print("(", end="")
            if self.leftChild is not None:
                self.leftChild.infix()
            print(self.data, end="")
            if self.rightChild is not None:
                self.rightChild.infix()
            if self.leftChild is not None or self.rightChild is not None:
                print(")", end="")

    def prefix(self):
        if self.data is not None:
            print(self.data, end="")
            if self.leftChild is not None:
                self.leftChild.prefix()
            if self.rightChild is not None:
                self.rightChild.prefix()

print(" *** Postfix to Infix and Prefix ***")
S = Stack()
inp = input('Enter Postfix : ')
for op in inp:
    if op in '+-*/':
        op2, op1 = S.pop(), S.pop()
        tmp = BinaryTree(op)
        tmp.add(leftChild=op1, rightChild=op2)
        S.push(tmp)
    else:
        S.push(BinaryTree(op))

expTree = S.pop()
expTree.print()
print('-' * 50)
print("Infix => ", end="")
expTree.infix()
print()
print("Prefix => ", end="")
expTree.prefix()
print("\n===== End of program =====")