class Node:
    def __init__(self, data, next=None):
        self._data = data
        self._next = next

class LinkedList:
    def __init__(self):
        self._head = None

    def append(self, data):
        new_node = Node(data)
        if self._head is None:
            self._head = new_node
        else:
            current = self._head
            while current._next is not None:
                current = current._next
            current._next = new_node

    def remove(self,ele):
        if self._head is None:
            return
        
        if self._head._data==ele:
            self._head=self._head._next
            return
        current=self._head
        while current._next is not None:
            if ele==current._next._data:
                break
            current=current._next
        if current._next is None:
            return
        else:
            current._next=current._next._next
                

    def __str__(self):
        if self._head is None:
            return "[[Empty Linked List]]"
        else:
            current = self._head
            self.result = []
            while current is not None:
                self.result.append(current._data)
                current = current._next
            return f'[[ {", ".join(map(str, sorted(self.result)))}]]'

class sortedLinkedList(LinkedList):
    ''' Ascending order Linked List '''
    def append(self, data):
        return super().append(data)
    
    def remove(self,ele):
        return super().remove(ele)

print(" *** Sorted Linked List (remove) ***")
inp = input("Enter data / remove-data : ")
data, rData = inp.split('/')
myList = sortedLinkedList()
for index, data in enumerate(data.split()):
    num = int(data)
    myList.append(data)
    # print(f"{index+1}. add {num} => {myList}")
print(f"myList => {myList}")
for index, data in enumerate(rData.split()):
    num = int(data)
    myList.remove(data)
    print(f"{index+1}. remove {num} => {myList}")

print(f"myList => {myList}")

print(" ===== End of program =====")