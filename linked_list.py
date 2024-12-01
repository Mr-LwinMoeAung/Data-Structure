#Linked list is a linear data structure.
#NOde = Data and Link             Data-Nextlink
#Data fill and two links   Prelink-Data-NextLink
#End node = Null

#Pros
#No need to mention the size of list
#Insert and remove is easy (Every Position)
#Implement the Stack Queue and Graph
#Represnet and Manipulate Polynomials
#Web Brower (Previous and next page)
#Music Player : Song are linked
#Image viewer : Image are linked 

#Cons:
#need extra memory
#Ramdon access not possible 

#Single linked list     :Add Delete Travelsal the element
#Begin : End : In between

#Double linked List
#Circular linked list

#Pratical 
#One Node : data and link
#Create two classes Node and linked Lists

# begin
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.ref=None

# class Link:
#     def __init__(self):
#         self.head=None
    
#     def start(self,data):
#         new_node=Node(data)
#         new_node.ref=self.head
#         self.head=new_node

#     def print(self):
#         if self.head is None:
#             print('It is empty')
#         else:
#             while self.head is not None:
#                 print(self.head.data,end=' ')
#                 self.head=self.head.ref

# n=Link()
# n.start(0)
# n.start(1)
# n.start(2)
# n.print()

# end
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class Linked_list:
    def __init__(self):
        self.head=None

    def begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node

    def print(self):
        if self.head is None:
            print('It is Empty')
        else:
            while self.head is not None:
                ans=print('',self.head.data,end=' ')
                print(ans)
                self.head=self.head.ref

ll=Linked_list()
ll.begin(0)
ll.begin(1)
ll.begin(2)
ll.end(10)
ll.begin(3)
ll.print()