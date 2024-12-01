class Node:
    def __init__(self,data,next=None):
        self._data = data
        self._next = None
        if next is not None:
            self._next = next

class LinkedList:
    def __init__(self):
        self._head = None

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
    
    def __add__(self,other):
        answer=f'[[ {self._foradd}, {other._foradd}]]'
        return answer
    
    def __str__(self):
        if self._head is None:
            return '[[Empty Linked List]]'
        else:
            self.result=[]
            current=self._head
            while current is not None:
                self.result.append(current._data)
                current=current._next
                self._foradd=f"{', '.join(map(str,self.result))}"
            return f"[[ {', '.join(map(str,self.result))}]]"
        
print(" *** Linked List ADD ***")
l1,l2 = input("Enter myList1 / myList2 : ").split('/')
myList1 = LinkedList()
myList2 = LinkedList()
for index, data in enumerate(l1.split()):
    myList1.append(data)
for index, data in enumerate(l2.split()):
    myList2.append(data)
print(f"myList1 => {myList1}")
print(f"myList2 => {myList2}")
print(f"myList1 + myList2 => {myList1+myList2}")
print(f"myList2 + myList1 => {myList2+myList1}")
print(" ===== End of program =====")