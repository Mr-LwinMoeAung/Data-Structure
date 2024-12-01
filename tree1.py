#Tree
#Collection of entities(Nodes) connected by edges
#Non-Linear Data Structure
#Can see relationship between Nodes

#Node
#RootNode -> Use to travel every nodes
#Edge
#Parent
#Child -> every node is Child Node except rootnode
#Sibling -> If same parent
#Leaf node,External Node,Terminal Node -> Has no children
#Internal Node,Non-terminal Node -> Has at least 1 child, Just Not leaf nodes
#Path -> Number of edges between Nodes

#N nodes = N-1 edges
#Child has 1 parent, Parent can have multiple
#Degree of Node = Number of children
#Degree of tree = Choose Highest Degree of a Node
#Level = start from Level 0 (root).
#Height of node = No. of edges from That node to leaf node(pick the longest)
#Height of tree = From root to leaf
#Depth of Node = No. of edges from that node to root
#Depth of tree = Pick the longest from root to leaf
#Depth of root node and Height of leaf node = 0

#General Tree = can have any no. of child node

#Binary search Tree = Searching purpose
#Can have at most 2 child

#1. Full binary tree
#2. Complete binary tree
#3. Perfect binary tree
#4. Balance binary tree
#5. Pathological binary tree

#1. Full binary tree or Stickly binary tree
#Every node has 0 or 2 child nodes
##Every nodes have 2 child , leaf has 0 in any level

#2. Complete binary tree
# all level except last level -> Completely fill with nodes
# Last level -> Complete fill or fill from left to right
## All level node have 2 child, Last level -> Complete fill or fill from left to right

#3. Perfect binary tree
#internal node = 2 child, leaf node same level

#4. Balanced binary tree
#Height of left and right subtree of every node differ at most 1
#diff = |height of left sub tree - height of right subtree|
#Height of empty tree = -1
##Every node
##|0-1|=1

#5. Pathological binary tree or Degenerate binary tree
#Every parent has 1 child



#Binary Search Tree *BST
#Main node -> start from root to every
#__main node__
#left node < main node < right node
## Above main must rule

#if equal = duplicate
#1 neglect
#2 #left node <= main node < right node
#3 #left node < main node <= right node

#Traversal
# use recursive

#Pre-order Traversal
# The root -> left sub-tree -> right sub-tree

#In-order Traversal
# left st -> root -> right st (ascending) (start at down)

#Post-order
# left st -> right st -> root

#Level-order
# order base on levels [start root(level 0)] left->right

#Max and Min value
# Node with largest value: right most child of the right subtree
# Node with smallest value : left most child of the left subtree
# Node in BST = no. of node LST + RST + 1

#When use Balanced BST -> insertion, deletion, searching can perform effiently

#Searching @
# BST==Empty : @ not present
# root==@ : present
# not : @ < root -> left subtree
       #@ > root -> right st

#Insertion
#1. BST empty? -> insert @ = root
#2. else: compare @ with root
# root < @ -> right 
# root > @ -> left

#Deletion
# Do Searching operation @
# 3 delete situation : 0 child node, 1 child node, 2 child node
# 0 child -> Search and delete
# 1 child -> Search and delete and attach(replace) the child with above
# 2 child -> 2 options: replace that deleted node with 
# largest value of left(LL) or smallest value of right


#Program BST (IMPLEMENT)
# Key(data), left child, right child 
# |left ref|key|right ref|



# The in-order successor is the smallest value in the right subtree of a node,
# and the in-order predecessor is the largest value in the left subtree.
# Balance BST => Searching, Insertion, Deletion ==> O(log(n))
# Unbalance BST => O(n)         === Worst Case


class BST:
    def __init__(self,key):
        self.key=key
        self.lc=None
        self.rc=None

    def insert(self,data):
        # if self.key is None:
        #     self.key=data
        #     return
        if self.key > data: 
            if self.lc:
                self.lc.insert(data)
            else:
                self.lc=BST(data)
        else:
            if self.rc:
                self.rc.insert(data)
            else:
                self.rc=BST(data)

    def preorder(self):
        print(self.key,end=' ')
        if self.lc:
            self.lc.preorder()
        if self.rc:
            self.rc.preorder()

    def inorder(self):
        if self.lc:
            self.lc.inorder()
        print(self.key,end=' ')
        if self.rc:
            self.rc.inorder()

    def postorder(self):
        if self.lc:
            self.lc.postorder()
        if self.rc:
            self.rc.postorder()
        print(self.key,end=' ')

    def search(self,data):
        if self.key==data:
            print('Node is found')
            return
        if data < self.key:
            if self.lc is None:
                print('Node is not present')
            else:
                self.lc.search(data)
        else:
            if self.rc is None:
                print('Node is not present')
            else:
                self.rc.search(data)

    def delete(self,data):
        if self.key is None:                                   #10
            print('Tree is empty')                      #6              98
            return                                  #3      #7
        if data<self.key:                        #1
            if self.lc:
                self.lc = self.lc.delete(data)
            else:
                print('Data is not present')
        elif data>self.key:
            if self.rc:
                self.rc=self.rc.delete(data)
            else:
                print('Data is not present')
        else:
            if self.lc is None:
                temp=self.rc
                self=None
                return temp
            
            if self.rc is None:
                temp=self.lc
                self=None
                return temp
            
            node = self.rc
            while node.lc:
                node = node.lc
            self.key=node.key
            self.rc=self.rc.delete(node.key)
        return self

root=BST(10)
list=[6,3,1,6,98,3,7]
for i in list:
    root.insert(i)
print('Preorder')
root.preorder()
print()
# print('Inorder')
# root.inorder()
# print()
# print('Postorder')
# root.postorder()
# root.search(6)
root.search(98)
root.delete(98)
print('After deleting....')
root.preorder()