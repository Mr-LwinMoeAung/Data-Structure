# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
    
#     def __str__(self):
#         return str(self.data)

# class BST:
#     def __init__(self):
#         self.root = None

#     def insert(self, data):
#         if self.root is None:
#             self.root = Node(data)
#         else:
#             self._insert_recursive(self.root, data)

#     def _insert_recursive(self, current_node, data):
#         if data < current_node.data:    
#             if current_node.left is None:
#                 current_node.left = Node(data)
#             else:
#                 self._insert_recursive(current_node.left, data)
#         else:
#             if current_node.right is None:
#                 current_node.right = Node(data)
#             else:
#                 self._insert_recursive(current_node.right, data)

#     def printTree(self, node, level = 0):
#         if node != None:
#             self.printTree(node.right, level + 1)
#             print('     ' * level, node)
#             self.printTree(node.left, level + 1)

# T = BST()
# inp = [int(i) for i in input('Enter Input : ').split()]
# for i in inp:
#     root = T.insert(i)
# T.printTree(T.root)



# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.right=None
#         self.left=None

#     def __str__(self):
#         return str(self.data)


# class BST:
#     def __init__(self):
#         self.root=None

#     def insert(self,ele):
#         if self.root is None:
#             self.root=Node(ele)
#         else:
#             self._insert(self.root,ele)

#     def _insert(self,current,ele):
#         if current.data > ele:
#             if current.left is None:
#                 current.left=Node(ele)
#             else:
#                 self._insert(current.left,ele)

#         else:
#             if current.right is None:
#                 current.right=Node(ele)
#             else:
#                 self._insert(current.right,ele)

#     def height(self):
#         return self._height(self.root)

#     def _height(self,current):
#         if current is None:
#             return -1
        
#         left_height=self._height(current.left)
#         right_height=self._height(current.right)
#         return max(left_height,right_height)+1
    

#     def print(self):
#         self._print(self.root,0)

#     def _print(self,current,level):
#         if current is not None:
#             self._print(current.left,level+1)
#             print('     '*level,current)
#             self._print(current.right,level+1)


# tree = BST()
# print(f" *** Height of Binary Search Tree ***")
# arr = list(map(int, input("Enter Input : ").split()))
# print(arr)
# for ele in arr:
#     tree.insert(ele)
# tree.print()
# print(f"Height of this tree = {tree.height()}")



# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.right=None
#         self.left=None

#     def __str__(self):
#         return str(self.data)

# class BST:
#     def __init__(self):
#         self.root=None

#     def insert(self,ele):
#         if self.root is None:
#             self.root=Node(ele)
#         else:
#             self._insert(self.root,ele)

#     def _insert(self,current,ele):
#         if current.data > ele:
#             if current.left is None:
#                 current.left=Node(ele)
#             else:
#                 self._insert(current.left,ele)

#         else:
#             if current.right is None:
#                 current.right=Node(ele)
#             else:
#                 self._insert(current.right,ele)

#     def height(self):
#         return self._height(self.root)

#     def _height(self,current):
#         if current is None:
#             return -1
        
#         left_height=self._height(current.left)
#         right_height=self._height(current.right)
#         return max(left_height,right_height)+1
    
#     def path2node(self,ele):
#         self._path2node(self.root,ele,[])

#     def _path2node(self,current,ele,target):
#         if current is None:
#             return

#         target.append(current.data)
    
#         if current.data == ele:
#             self.pp(target)
#         elif current.data>ele:
#                 self._path2node(current.left,ele,target)
#         elif current.data<ele:
#                 self._path2node(current.right,ele,target)
    
#     def pp(self,path):
#         if len(path) is not None:
#             print(f'Path from root to {path[-1]} ==> {"->".join(map(str,path))}')

#     def print(self):
#         self._print(self.root,0)

#     def _print(self,current,level):
#         if current is not None:
#             self._print(current.right,level+1)
#             print('     '*level,current)
#             self._print(current.left,level+1)

# tree = BST()
# print(" *** Node Path (Binary Search Tree) ***")
# inp,target = input("Enter data : ").split("/")
# inputData = inp.split()
# tree = BST()
# for ele in inputData:
#     tree.insert(int(ele))
# tree.print()
# for ele in target.split():
#     data = int(ele)
#     tree.path2node(data)
# print("===== End of program =====")


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

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

    def delete(self,ele):
        self.root=self._delete(self.root,ele)

    def _delete(self,current,ele):
        if current is None:
            return current
        
        elif current.data>ele:
            if current.left:
                current.left=self._delete(current.left,ele)
            else:
                print("Invalid")
            
        elif current.data<ele:
            if current.right:
                current.right=self._delete(current.right,ele)
            else:
                print('Invalid')
        
        else:
            if not current.left:
                temp=current.right
                current=None
                return temp
            
            if not current.right:
                temp=current.left
                current=None
                return temp
            
            node=current.right
            while node.left:
                node=node.left
            current.data=node.data
            current.right=self._delete(current.right,node.data)
        return current

    def print(self):
        self._print_rotated(self.root, 0)

    def _print_rotated(self, node, level):
        if node is not None:
            self._print_rotated(node.right, level + 1)
            print('     ' * level, str(node))
            self._print_rotated(node.left, level + 1)


print(" *** Binary Search Tree (insert/delete) ***")
tree = BST()
data = input("Enter Input : ").split("/")
for command in data:
    cmd,*values = command.split()
    values =[int(e) for e in values]
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