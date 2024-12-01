class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        if key < current_node.data:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursive(current_node.left, key)
        else:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursive(current_node.right, key)

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


class AVL(BST):

    def __init__(self):
        super().__init__()

    def balance_factor(self, value: int) -> int:
        return self._balance_factor(self.root, value)

    def _balance_factor(self, root, data=None):
        if root is None:
            return 0

        if data is None:
            left_height = self._height(root.left)
            right_height = self._height(root.right)
            return left_height - right_height

        if data is not None:
            if root.data == data:
                return self._balance_factor(root)
            elif data < root.data:
                return self._balance_factor(root.left, data)
            else:
                return self._balance_factor(root.right, data) 

    def height(self, data=None):
        return self._height(self.root, data)

    def _height(self, root, data=None):
        if root is None:
            return -1
        if data is None:
            left_height = self._height(root.left)
            right_height = self._height(root.right)
            return max(left_height, right_height) + 1

        if data is not None:
            if root.data == data:
                return self._height(root)
            elif data < root.data:
                return self._height(root.left, data)
            else:
                return self._height(root.right, data)


print(" *** Adelson-Velskii Landis (AVL) Tree (insert/delete) ***")
tree = AVL()
data, value = input("Enter inputs / value: ").split("/")
for ele in data.split():
    tree.insert(int(ele))
tree.printTree(tree.root)
print("-"*50)
print(f"tree height => {tree.height()}")
print(f"Height of {value} => {tree.height(int(value))}")
print(f"Balance factor of {value} => {tree.balance_factor(int(value))}")

print("===== End of program ======")