class Queue:
    def __init__(self):
        self.box=[]
        self.check=0
    
    def enqueue(self,data):
        self.box.append(data)

    def dequeue(self):
        return self.box.pop(0)

    def size(self):
        self.check+=1
        return f'{self.check:2}'

    def __len__(self):
        return len(self.box)

    def __str__(self):
        return f'[{self.box}]'

print(' *** Queue Journey ***')
inp=input('Enter people : ').split('-')
main=Queue()
q1=Queue()
q2=Queue()
count=0

print('minute => [ Main Queue ] == [ Queue-1 ] == [ Queue-2]')
print(' 0 =>',f'[{inp}]','==','[[]]','==','[[]]')

for i in inp:
    main.enqueue(i)

for i in range(len(main)):
    test=[]
    if count==3 or (count==6 and len(q1)==5):
        q1.dequeue()
    mainpop=main.dequeue()
    if len(q1)<5:
        q1.enqueue(mainpop)
    else:
        q2.enqueue(mainpop)

    if len(q2)==3:
        q2.dequeue()
        q1.dequeue()
        q2pop=q2.box.pop(-1)
        q1.enqueue(q2pop)
    
    count+=1
    print(f'{main.size()} => {main} == {q1} == {q2}')

print(' ===== End of program =====')