# Push : String or List
# Pop : Replace or Pop or Remove
# finding index = box.index(a)
# List can't use replace


class Node:
    def __init__(self, data, next=None):
        self._data = data
        self._next = next

class LinkedList:
    def __init__(self):
        self._head = None

    def appenddd(self, data):
        new_node = Node(data)
        if self._head is None:
            self._head = new_node
        else:
            current = self._head
            while current._next is not None:
                current = current._next
            current._next = new_node

    def __str__(self):
        if self._head is None:
            return "[[Empty Linked List]]"
        else:
            current = self._head
            result = []
            while current is not None:
                result.append(current._data)
                current = current._next
            return f'[[ {", ".join(map(str, sorted(result)))}]]'

class sortedLinkedList(LinkedList):
    ''' Ascending order Linked List '''
    def appenddd(self, data):
        return super().appenddd(data)

print(" *** Sorted Linked List ***")
inp = input("Enter data : ")
myList1 = sortedLinkedList()
for index, data in enumerate(inp.split()):
    num = int(data)
    myList1.appenddd(data)
    print(f"{index+1}. add {num} => {myList1}")
print(f"myList1 => {myList1}")
print(" ===== End of program =====")