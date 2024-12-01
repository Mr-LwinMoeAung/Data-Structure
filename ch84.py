class Node:
    def __init__(self, data):
        self.data, self.left, self.right, self.height = data, None, None, 0

    def __str__(self):
        return str(self.data)


class AVL:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)
        return self.root

    def _insert(self, root, data):
        if root is None:
            return Node(data)

        attr = "left" if data < root.data else "right"
        setattr(root, attr, self._insert(getattr(root, attr), data))
        return root

    def print(self):
        return self.printTree(self.root)

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

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

    def get_parent(self, node):
        return self._get_parent(self.root, node)

    def _get_parent(self, root, node):
        if root is None or (root.left is None and root.right is None):
            return None

        if root.left and root.left.data == node:
            return root.data

        elif root.right and root.right.data == node:
            return root.data

        if node < root.data:
            return self._get_parent(root.left, node)
        else:
            return self._get_parent(root.right, node)

    def left_rotate(self, value: int):
        return self._left_rotate(self.root, value)

    def right_rotate(self, value: int):
        return self._right_rotate(self.root, value)

    def _right_rotate(self, root, value):
        if root is None or (root.left is None and root.right is None):
            return root

        if self.root.data == value:
            new_root = root.left
            new_root.right = root
            new_root.left = root.left.left
            root.left = None
            root.right = None
            return new_root

        if root.left and root.left.data == value:
            new_root = root.left
            if new_root.left is None or (new_root.left.left is None and new_root.left.right is None):
                print("Invalid Rotation !!!")
                return new_root
            elif new_root.left.right and new_root.left.right.data > new_root.left.data and new_root.right is None:
                mid_root = new_root.left.right
                new_root.left.right = None
                mid_root.left = new_root.left
                mid_root.right = new_root
                root.left = mid_root
                new_root.left = None
                new_root = None
                return root
            else:
                temp = new_root.left.right
                mid_root = new_root.left
                mid_root.right = new_root
                mid_root.right.left = temp
                root.left = mid_root
                return root

        elif root.right and root.right.data == value:
            print("Invalid Rotation !!!")
            return

        if value < root.data:
            return self._right_rotate(root.left, value)
        else:
            return self._right_rotate(root.right, value)

    def _left_rotate(self, root, value):
        if root is None or (root.left is None and root.right is None):
            return root

        if self.root.data == value:
            new_root = root.right
            new_root.left = root
            new_root.right = root.right.right
            root.left = None
            root.right = None
            return new_root

        if root.right and root.right.data == value:
            new_root = root.right
            if new_root.right is None or new_root.right.right is None:
                print("Invalid Rotation !!!")
                return new_root
            root.right = new_root.right
            root.right.left = new_root
            new_root.left = None
            new_root.right = None
            return new_root
        elif root.left and root.left.data == value:
            print("Invalid Rotation !!!")
            return

        if value < root.data:
            return self._left_rotate(root.left, value)
        else:
            return self._left_rotate(root.right, value)

    def reBalance(self, node):
        if node is not None:
            self.root = self._reBalance(self.root, node)

    def _reBalance(self, root, node):
        if root is None:
            return None

        balance_factor = self._balance_factor(root)
        if balance_factor > 1:
            balance_factor = self._balance_factor(root.left)
            if balance_factor > 1:
                root = root.left
                return self.right_rotate(root.data)
            return self.right_rotate(root.data)
        elif balance_factor == 1:
            balance_factor = self._balance_factor(root.left)
            if balance_factor > 1:
                root = root.left
                return self.right_rotate(root.data)
            return root
        elif balance_factor < -1:
            return self.left_rotate(root.data)
        return root


print(" *** Adelson-Velskii Landis (AVL) Tree (rebalance) ***")
tree = AVL()
data, value = input("Enter inputs / value: ").split("/")
for ele in data.split():
    tree.insert(int(ele))
tree.print()
print("-" * 20)
print(f"tree height => {tree.height()}")
print("-" * 20)
node = tree.insert(int(value))
tree.print()
print("-" * 20)
print(f"Adding {value.replace(' ','')} height => {tree.height()}")
print("-" * 20)
tree.reBalance(node)
tree.print()
print("-" * 20)
print(f"After rebalance tree height => {tree.height()}")
print("-" * 20)

print("===== End of program ======")