class Stack:
    def __init__(self):
        self.box=[]

    def push(self, item):
        self.box=item

    def pop(self):
        count=1
        for i in range(len(self.box)):
            for j,find in enumerate(self.box):
                if i!=len(self.box)-1:
                    j=i+count
                    count+=1
                if self.box[i]<self.box[j]:
                    self.box[i]=self.box[j]
                    count=1
                    break                    
        self.box[-1]=-1

def find_next_greater_elements(arr):
    stack = Stack()
    result = []
    result=arr.copy()
    stack.push(result)
    stack.pop()
    return result

print(" *** Next Greater Element ***")
inp = input("Enter list of number : ")
inp = [int(ele) for ele in inp.split()]
print(inp)
next_greater = find_next_greater_elements(inp)
print(next_greater) 