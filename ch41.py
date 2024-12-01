class Queue:

    def __init__(self):
        self._items = list()
    
    def enqueue(self,ele):
        try:
            ele=int(ele)
        except:
            ele=ele
        self._items.append(ele)
    
    def size(self):
        return len(self._items)
    
    def __str__(self):
        return f'[{self._items}]'

print(" *** Basic Queue ***")
items = input("Enter items : ").split()
print(f"items={items}")
q = Queue()
for idx,ele in enumerate(items):
    print(f"{idx+1} = {ele}")
    q.enqueue(ele)
    print(f"size={q.size()} => {q} ")
print(" ===== End of program =====")