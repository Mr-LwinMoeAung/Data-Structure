class queue:
    def __init__(self):
        self.box=list()

    def enqueue(self,data):
        self.box.append(data)

    def dequeue(self):
        if self.isEmpty()==False:
            self.box.pop(0)
        
    def isEmpty(self):
        return len(self.box)==0

    def size(self):
        return len(self.box)
    
    def first(self):
        if self.isEmpty()==False:
            return self.box[0]
    
    def last(self):
        if self.isEmpty()==False:
            return self.box[-1]
    
    def __str__(self):
        ans=''
        for i in self.box:
            ans+=i+' '
        return f'Data in queue is : {ans}'

print(' *** Basic Queue 3 ***')
inp=input('Enter Input : ').split(',')
print(f'inp={inp}')
q1=queue()

for i in inp:
    comamnd = i[:2].upper()
    if comamnd == "EN":
        data = i[3:].strip()
        q1.enqueue(data)
    elif comamnd == "DE":
        q1.dequeue()
    elif comamnd == "IE":
        print("Queue empty = {0}".format(q1.isEmpty()))
    elif comamnd == "SI":
        print("Queue size = {0}".format(q1.size()))
    elif comamnd == "FI":
        print("First of queue = {0}".format(q1.first()))
    elif comamnd == "LA":
        print("Last of queue = {0}".format(q1.last()))
    elif comamnd == "PR":
        print(q1)

print(' ===== End of program =====')