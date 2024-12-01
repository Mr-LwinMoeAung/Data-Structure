class Stack():
    
    def __init__(self):
        self.box=[] 
        
    def push(self,ele):
        for i in ele:
            try:
                i=int(i)
                self.box.append(i)
            except:
                self.box.append(i)
        
    def pop(self):
        for i,find in enumerate(self.box):
            if isinstance(find,str):
                num1=self.box[i-2]
                num2=self.box[i-1]
                ans=eval(f'num1 {find} num2')
                self.box.insert(i+1,ans)
                self.box[i-2]='@'
                self.box[i-1]='@'
                while '@' in self.box:
                    self.box.remove('@')
                self.box.remove(find)
                return Stack.pop(self)
        ans=float(self.box[0])
        print(f'Answer :  {ans:0.2f}')

def postFixeval(st):
    s = Stack()
    s.push(st)
    return s.pop()

            

print(" ***Postfix expression calcuation***")
token = list(input("Enter Postfix expression : ").split())
postFixeval(token)