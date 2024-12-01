class Node:
    def __init__(self,data,next=None):
        self._data = data
        self._next = None
        if next is not None:
            self._next = next

class LinkedList:
    def __init__(self):
        self._head = None

    def lists(self):
        self.string=' '
        self._ansbox=list()
        self._box=list()

    def append(self,data):
        self._box.append(data)
        new_node = Node(data)
        if self._head is None:
            self._head=new_node
        else:
            n=self._head
            while n._next is not None:
                n=n._next
            n._next=new_node

    def size(self):
        return len(self._box)
    
    def __str__(self):
        if self._head is None:
            return '[[Empty Linked List]]'
        else:
            while self._head is not None:
                ans=self._head._data
                self.string+=str(ans)+', '
                answer=f'[[{self.string}'
                answer=answer[0:len(answer)-2]
                self._head=self._head._next
                return f'{answer}]]'

print(" *** Basic Linked List ***")
inp = input("Enter data : ")
myList = LinkedList()
myList.lists()
print(f"{myList.size()} => {myList}")
for d in inp.split():
    myList.append(d)
    print(f"{myList.size()} => {myList}")
print(" ===== End of program =====")
