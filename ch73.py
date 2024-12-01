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
                
    def path2node(self, target):
        self._path2node_recursive(self.root, target, [])

    def _path2node_recursive(self, current_node, target, path):
        if current_node is None:
            return

        path.append(current_node.val)

        if current_node.val == target:
            self._print_path(path)
        elif target < current_node.val:
            self._path2node_recursive(current_node.left, target, path)
        else:
            self._path2node_recursive(current_node.right, target, path)

        path.pop()

    def _print_path(self, path):
        if len(path) > 0:
            print(f"Path from root to node {path[-1]} ==> {' -> '.join(map(str, path))}")

    def print(self):
        self._print_rotated(self.root, 0)

    def _print_rotated(self, node, level):
        if node is not None:
            self._print_rotated(node.right, level + 1)
            print('     ' * level, str(node))
            self._print_rotated(node.left, level + 1)

tree = BST()
print(" *** Node Path (Binary Search Tree) ***")
inp, target = input("Enter data : ").split("/")
inputData = inp.split()
for ele in inputData:
    tree.insert(int(ele))
tree.print()
for ele in target.split():
    data = int(ele)
    tree.path2node(data)
print("===== End of program =====")
