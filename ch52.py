class Node:
    def __init__(self,data,next=None):
        self._data = data
        self._next = None
        if next is not None:
            self._next = next

class LinkedList:
    def __init__(self):
        self._head = None

    def addHead(self,data):
        new_node=Node(data)
        new_node._next=self._head
        self._head=new_node

    def append(self,data):
        new_node = Node(data)
        if self._head is None:
            self._head=new_node
        else:
            n=self._head
            while n._next is not None:
                n=n._next
            n._next=new_node

    def size(self):
        count=0
        current=self._head
        while current is not None:
            count+=1
            current = current._next
        return count
    
    def __str__(self):
        if self._head is None:
            return '[[Empty Linked List]]'
        else:
            result=[]
            current=self._head
            while current is not None:
                result.append(current._data)
                current=current._next
            return f"[[ {', '.join(map(str,result))}]]"
                
            
print(" *** Basic Linked List ***")
inp = input("Enter data : ")
myList = LinkedList()
print(f"{myList.size()} => {myList}")
for index, data in enumerate(inp.split()):
    if index%2 == 0:
        myList.append(data)
    else:
        myList.addHead(data)
    print(f"{myList.size()} => {myList}")

print(" ===== End of program =====")