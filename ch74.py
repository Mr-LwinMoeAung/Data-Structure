class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.data)
    
class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.re_in(self.root, data)

    def re_in(self, current, data):
        if current.data > data:
            if current.left is None:
                current.left = Node(data)
            else:
                self.re_in(current.left, data)
        else:
            if current.right is None:
                current.right = Node(data)
            else:
                self.re_in(current.right, data)

    def delete(self, data):
        self.root = self.re_delete(self.root, data)

    def re_delete(self, current, data):
        if current is None:
            return current

        if data < current.data:
            if current.left:
                current.left = self.re_delete(current.left, data)
            else:
                print(f'{data} Not present')
        elif data > current.data:
            if current.right:
                current.right = self.re_delete(current.right, data)
            else:
                print(f'{data} Not present')
        else:
            if current.left is None:
                temp = current.right
                current = None
                return temp
            elif current.right is None:
                temp = current.left
                current = None
                return temp
            temp = self.min_value_node(current.right)
            current.data = temp.data
            current.right = self.re_delete(current.right, temp.data)

        return current

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def print(self):
        self.re_print(self.root)

    def re_print(self, current, level=0):
        if current is not None:
            self.re_print(current.right, level + 1)
            print('     ' * level, current)
            self.re_print(current.left, level + 1)

print(" *** Binary Search Tree (insert/delete) ***")
tree = BST()
data = input("Enter Input : ").split("/")
for command in data:
    cmd, *values = command.split()
    values = [int(e) for e in values]
    if cmd == "i":
        print(f"Inserting . . . {values}")
        for ele in values:
            tree.insert(int(ele))
    elif cmd == "d":
        print(f"Deleting . . . {values}")
        for ele in values:
            tree.delete(int(ele))
    tree.print()
print("===== End of program ======")