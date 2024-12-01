class Queue:
    def __init__(self):
        self.box=[]
        self.n=int(n)

    def enqueue(self,ele):
        self.box.append(ele)

    def dequeue(self):
        return self.box.pop(0)

    def size(self):
        return len(self.box)

    def __len__(self):
        return self.n
    
    def __str__(self):
        return f'[{self.box}]'
    
print(" *** Basic Queue enqueue/dequeue***")
items,n = input("Enter items / n : ").split('/')
print(f"items = {items}")
print(f"n = {n.strip()}")
q1 = Queue()
q2 = Queue()
for idx,ele in enumerate(items.split()):
    # print(f"{idx+1} = {ele}")
    q1.enqueue(ele)
print(f"q1 => {q1}\n")
for _ in range(len(q1)):
    item = q1.dequeue()
    q2.enqueue(item)
    if q2.size() >= int(n):
        break
print(f"q1 => {q1} ")
print(f"q2 = {q2}")

print(" ===== End of program =====")