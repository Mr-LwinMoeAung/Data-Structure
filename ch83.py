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

    def print(self, node, level=0):
        if node is not None:
            self.print(node.right, level + 1)
            print('     ' * level, node)
            self.print(node.left, level + 1)

class AVL(BST):
    def __init__(self):
        super().__init__()

    def balance_factor(self, value):
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

    def get_parent(self, value):
        return self._get_parent_recursive(self.root, None, value)

    def _get_parent_recursive(self, current_node, parent, value):
        if current_node is None:
            return None

        if current_node.data == value:
            return parent

        if value < current_node.data:
            return self._get_parent_recursive(current_node.left, current_node, value)
        else:
            return self._get_parent_recursive(current_node.right, current_node, value) 

    def left_rotate(self, value):
        node_to_rotate = self.find_node(self.root, value)

        if node_to_rotate is None:
            print('Invalid Rotation!!')
            return

        
        if node_to_rotate.right is None:
            print('Invalid Rotation!!')
            return

        new_root = node_to_rotate.right
        node_to_rotate.right = new_root.left
        new_root.left = node_to_rotate

        parent = self.get_parent(value)
        if parent:
            if parent.left == node_to_rotate:
                parent.left = new_root
            else:
                parent.right = new_root
        else:
            self.root = new_root

    def right_rotate(self, value):
        # Find the node to rotate
        node_to_rotate = self.find_node(self.root, value)

        if node_to_rotate is None:
            print('Invalid Rotation !!!')
            return

        # Check if the left child of the node to rotate exists
        if node_to_rotate.left is None:
            print('Invalid Rotation !!!')
            return
        
        if value == 1:
            if node_to_rotate.right is None:
                print('Invalid Rotation !!!')
                return

        new_root = node_to_rotate.left
        node_to_rotate.left = new_root.right
        new_root.right = node_to_rotate

        # Update the parent of the rotated node
        parent = self.get_parent(value)
        if parent:
            if parent.left == node_to_rotate:
                parent.left = new_root
            else:
                parent.right = new_root
        else:
            self.root = new_root

    def find_node(self, root, value):
        if root is None:
            return None

        if value == root.data:
            return root

        if value < root.data:
            return self.find_node(root.left, value)
        else:
            return self.find_node(root.right, value)       

print(" *** Adelson-Velskii Landis (AVL) Tree (right rotatation) ***")
tree = AVL()
data, value = input("Enter inputs / value: ").split("/")
for ele in data.split():
    tree.insert(int(ele))
tree.print(tree.root)
print("-" * 50)
print(f"tree height => {tree.height()}")
print(f"Height of {value} => {tree.height(int(value))}")
print(f"Balance factor of {value} => {tree.balance_factor(int(value))}")
print(f"Parent of {value} => {tree.get_parent(int(value))}")
print("-" * 50)
tree.right_rotate(int(value))
tree.print(tree.root)
print(f"tree height => {tree.height()}")
print(f"Height of {value} => {tree.height(int(value))}")
print(f"Balance factor of {value} => {tree.balance_factor(int(value))}")
print(f"Parent of {value} => {tree.get_parent(int(value))}")
print("===== End of program ======")