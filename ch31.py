class Stack():
    def __init__(self):
        self.box=[]
    def push(self,i):
        self.box.append(i)
    def pop(self):
        self.box.pop()
    def top(self):
        pass
    def peek(self):
        pass
    def isEmpty(self):
        return len(self.box)==0
    def size(self):
        return (f'{len(self.box)}')
    def __str__(self):
        return f'{self.box}'
    
print(" *** Stack implement by Python list***")
inp = [ele for ele in input("Enter data to stack : ").split()]
s = Stack()
for ele in inp:
    s.push(ele)
print(s.size(),"Data in stack : ",s)
while not s.isEmpty():
    s.pop()
print(s.size(),"Data in stack : ",s)