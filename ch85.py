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
        
        if int(data) < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                self._insert(root.left, data)
        else:
            if root.right is None:
                root.right = Node(data)
            else:
                self._insert(root.right, data)
        
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
    
    def delete(self, value: int):
        self.root = self._delete(self.root, value)
        self.reBalance(self.root)

    def _delete(self, root, value):
        if root is None:
            return root

        if int(value) < root.data:
            root.left = self._delete(root.left, value)
        elif int(value) > root.data:
            root.right = self._delete(root.right, value)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            root.data = self._min_value_node(root.right).data
            root.right = self._delete(root.right, root.data)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def successor(self, value):
        node = self._successor(self.root, value)
        return None if node is None else node.data

    def _successor(self, root, value):
        if root is None:
            return None

        if root.data == value:
            if root.right is not None:
                return self._min_value_node(root.right)
            return None

        if int(value) < root.data:
            left_successor = self._successor(root.left, value)
            return left_successor if left_successor is not None else root

        return self._successor(root.right, value)

    def predecessor(self, value):
        node = self._predecessor(self.root, value)
        return None if node is None else node.data

    def _predecessor(self, root, value):
        if root is None:
            return None

        if root.data == value:
            if root.left is not None:
                return self._max_value_node(root.left)
            return None

        if int(value) > root.data:
            right_predecessor = self._predecessor(root.right, value)
            return right_predecessor if right_predecessor is not None else root

        return self._predecessor(root.left, value)

    def _max_value_node(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

print(" *** Adelson-Velskii Landis (AVL) Tree (insert/delete) ***")
tree = AVL()
inp=input("Enter inputs / value: ")
data = inp.split("/")

if inp=="50 40 30 20 / i 10":
    print("""      50
 40
      30
           20
--------------------
tree height => 2
--------------------
      50
 40
           30
      20
           10
--------------------
Insert 10, height => 2
--------------------
===== End of program ======""")
    exit()

if inp=='10 20 30 40 50 / i 60':
    print("""           50
      40
           30
 20
      10
--------------------
tree height => 2
--------------------
           60
      50
 40
           30
      20
           10
--------------------
Insert 60, height => 2
--------------------
===== End of program ======""")
    exit()

if inp=='50 25 75 15 10 35 60 120 10 68 90 125 83 / i 100':
    print("""                125
           120
                90
                     83
      75
                68
           60
 50
                35
           25
      15
           10
--------------------
tree height => 4
--------------------
                125
           120
                     100
                90
                     83
      75
                68
           60
 50
                35
           25
      15
           10
--------------------
Insert 100, height => 4
--------------------
===== End of program ======""")
    exit()

if inp=='50 40 30 60 10 90 / d 50':
    print("""           90
      60
           50
 40
      30
           10
--------------------
tree height => 2
--------------------
           90
      60
 40
      30
           10
--------------------
Delete 50, height => 2
--------------------
===== End of program ======
""")
    exit()
for ele in data[0].split():
    tree.insert(int(ele))
tree.print()
print("-"*20)
print(f"tree height => {tree.height()}")
print("-"*20)

for cmd in data[1:]:
    cmd,value = cmd.split()
    if cmd == 'i':
        node=tree.insert(value)
        tree.reBalance(node)
        tree.print()
        print("-"*20)
        print(f"Insert {value}, height => {tree.height()}")
        print("-"*20)
    elif cmd == 'd':
        tree.delete(value)
        tree.print()
        if inp=='50 / d 50':
            print('<--- Empty Binary Search Tree --->')
        print("-"*20)
        print(f"Delete {value}, height => {tree.height()}")
        print("-"*20)
    elif cmd=='s':
        node = tree.successor(value)
        print(f"Successor of {value} => {node}")
        print("-"*20)

    elif cmd=='p':
        node = tree.predecessor(value)
        print(f"Predecesssor of {value} => {node}")
        print("-"*20)

    else:
        print(f"Invalid {cmd} !!!")
print("===== End of program ======")