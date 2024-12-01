#Height of each node may be a question

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self):
        return str(self.val)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        if key < current_node.val:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursive(current_node.left, key)
        else:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursive(current_node.right, key)

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return 0
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return max(left_height, right_height) + 1

    def print(self):
        print("Height of this tree =", self.height()-1)
        self._print_rotated(self.root, 0)

    def _print_rotated(self, node, level):
        if node is not None:
            self._print_rotated(node.right, level + 1)
            print('     ' * level, str(node))
            self._print_rotated(node.left, level + 1)

tree = BST()
print(" *** Height of Binary Search Tree ***")
arr = list(map(int, input("Enter Input : ").split()))
for ele in arr:
    tree.insert(ele)
    
print(arr)
tree.print()
print('===== End of program =====')