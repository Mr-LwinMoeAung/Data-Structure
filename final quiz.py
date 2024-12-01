#  *** Basic Linked List ***
# Enter data : 1 2 3
# 0 => [[Empty Linked List]]
# 1 => [[ 1]]
# 2 => [[ 1, 2]]
# 3 => [[ 1, 2, 3]]
#  ===== End of program =====

# class Node:
#     def __init__(self,data,next=None):
#         self.data = data
#         self.next = None
#         if next is not None:
#             self.next = next


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self,data):
#         new_node=Node(data)
#         if self.head is None:
#             self.head=new_node
#         else:
#             current = self.head
#             while current.next is not None:
#                 current=current.next
#             current.next=new_node

#     def size(self):
#         current = self.head
#         count=0
#         while current is not None:
#             count+=1
#             current=current.next
#         return count
                    
#     def __str__(self):
#         current = self.head
#         result=[]
#         if current is None:
#             return "Empty"
#         while current is not None:    
#             result.append(current.data)
#             current = current.next

#         return f"[[{', '.join(map(str,result))}]]"
    
 
# print(" *** Basic Linked List ***")
# inp = input("Enter data : ")
# myList = LinkedList()
# print(f"{myList.size()} => {myList}")
# for d in inp.split():
#     myList.append(d)
#     print(f"{myList.size()} => {myList}")
# print(" ===== End of program =====")



# class Node:
#     def __init__(self,data,next=None):
#         self.data = data
#         self.next = None
#         if next is not None:
#             self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self,data):
#         new_node=Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next is not None:
#                 current = current.next
#             current.next = new_node

#     def addHead(self,data):
#         new_node=Node(data)
#         new_node.next=self.head
#         self.head=new_node

#     def size(self):
#         current=self.head
#         count=0
#         while current is not None:
#             count+=1
#             current = current.next

#         return count
    
#     def __str__(self):
#         current = self.head
#         result=[]
#         if current is None:
#             return 'EMPTY'
#         else:
#             while current is not None:
#                 result.append(current.data)
#                 current=current.next
            
#             return f"{', '.join(map(str,result))}"



# print(" *** Basic Linked List ***")
# inp = input("Enter data : ")
# myList = LinkedList()
# print(f"{myList.size()} => {myList}")
# for index, data in enumerate(inp.split()):
#     if index%2 == 0:
#         myList.append(data)
#     else:
#         myList.addHead(data)
#     print(f"{myList.size()} => {myList}")

# print(" ===== End of program =====")




# class Node:
#     def __init__(self,data,next=None):
#         self.data = data
#         self.next = None
#         if next is not None:
#             self.next = next


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self,data):
#         new_node=Node(data)
#         if self.head is None:
#             self.head=new_node
#         else:
#             current = self.head
#             while current.next is not None:
#                 current=current.next
#             current.next=new_node

#     def size(self):
#         current = self.head
#         count=0
#         while current is not None:
#             count+=1
#             current=current.next
#         return count
    
#     def __add__(self,other):
#         return self.foradd + other.foradd
                    
#     def __str__(self):
#         current = self.head
#         result=[]
#         if current is None:
#             return "Empty"
#         while current is not None:    
#             result.append(current.data)
#             current = current.next
#             self.foradd=f"[[{', '.join(map(str,result))}]]"

#         return f"[[{', '.join(map(str,result))}]]"

# print(" *** Linked List ADD ***")
# l1,l2 = input("Enter myList1 / myList2 : ").split('/')
# myList1 = LinkedList()
# myList2 = LinkedList()
# for index, data in enumerate(l1.split()):
#     myList1.append(data)
# for index, data in enumerate(l2.split()):
#     myList2.append(data)
# print(f"myList1 => {myList1}")
# print(f"myList2 => {myList2}")
# print(f"myList1 + myList2 => {myList1+myList2}")
# print(f"myList2 + myList1 => {myList2+myList1}")
# print(" ===== End of program =====")



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
#             self._insert(self.root,data)

#     def _insert(self,current,data):
#         if data < current.data:
#             if current.left is None:
#                 current.left=Node(data)
#             else:
#                 self._insert(current.left,data)

#         else:
#             if current.right is None:
#                 current.right=Node(data)
#             else:
#                 self._insert(current.right,data)

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
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.data = key

#     def __str__(self):
#         return str(self.data) 

# class BST:
#     def __init__(self):
#         self.root = None

#     def insert(self, data):
#         if self.root is None:
#             self.root = Node(data)
#         else:
#             self._insert(self.root,data)

#     def _insert(self,current,data):
#         if data < current.data:
#             if current.left is None:
#                 current.left=Node(data)
#             else:
#                 self._insert(current.left,data)

#         else:
#             if current.right is None:
#                 current.right=Node(data)
#             else:
#                 self._insert(current.right,data)

#     def height(self,data=None):
#         return self._height(self.root,data)

#     def _height(self,current,data=None):
#         if current is None:
#             return -1
#         if data is None:
#             hleft=self._height(current.left)
#             hright=self._height(current.right)
#             return max(hleft,hright)+1
        
#         if data is not None:
#             if data==current.data:
#                 return self._height(current)
#             elif data<current.data:
#                 return self._height(current.left,data)
#             elif data>current.data:
#                 return self._height(current.right,data)


#     def print(self):
#         self._print(self.root,0)
    
#     def _print(self,current,level):
#         if current is not None:
#             self._print(current.right,level+1)
#             print('     '*level,str(current))
#             self._print(current.left,level+1)

# tree = BST()
# print(f" *** Height of Binary Search Tree ***")
# arr = list(map(int, input("Enter Input : ").split()))
# print(arr)
# for ele in arr:
#     tree.insert(ele)
# tree.print()
# print(f"Height of this tree = {tree.height()}")
# print(tree.height(2))




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

    def delete(self,data):
        self.root=self._delete(self.root,data)

    def _delete(self,current,data):
        if current is None:
            return
        elif current.data > data:
            if current.left:
                current.left=self._delete(current.left,data)
            else:
                print("No")
        elif current.data<data:
            if current.right:
                current.right=self._delete(current.right,data)
            else:
                print("No")
        else:
            if current.left is None:
                temp=current.right
                current=None
                return temp
            if current.right is None:
                temp=current.left
                current=None
                return temp
            
            node=current.right
            while node.left is not None:
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