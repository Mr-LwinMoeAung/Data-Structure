class Queue:
    def __init__(self):
        self.box=list()
        self.time_list=list()
        self.sort=[]
    
    def enqueue(self,data):
        self.box.append(data)

    def time(self):
        self.ans=0
        for i,j in enumerate(self.box):
            self.ans+=j
            self.time_list.append(self.ans)
        print(self.time_list)
            
    def dequeue(self):
        self.box.pop(0)

    def __str__(self):
        return f'{self.box}   {self.time_list}'

print(' *** Coffee Cafe ***')
inp=input('Enter minute-time : ').split()
print(inp)
q1=Queue()
q2=Queue()
new,final=[],[]

for i in inp:
    new.append(i.split('-'))
for i in new:
    for index,j in enumerate(i):
        if index%2!=0:
            final.append(int(j))
print(final)


for index,data in enumerate(final):
    if index==0:
        check1=data
        q1.enqueue(data)
    if index==1:
        check2=data
        q2.enqueue(data)
    if index!=0 and index!=1 and check1>check2:
        check2+=data
        q2.enqueue(data)
    elif index!=0 and index!=1 and check1<check2:
        check1+=data
        q1.enqueue(data)

q1.time()
q2.time()

# print(q1)
# print(q2)
arr=[]
    

for i in q1.time_list:
    arr.append(i)
for i in q2.time_list:
    arr.append(i)



print(arr)
arr_done=sorted(arr)
print(arr_done)

li=[]
 
for i in range(len(arr)):
      li.append([arr[i],i])
li.sort()
sort_index = []
 
for x in li:
      sort_index.append(x[1])
 
print(sort_index)


for i in arr_done:
    print(f'Time {i}, customer gets a cup of coffee. ')
