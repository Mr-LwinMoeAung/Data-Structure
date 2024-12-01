class Stack():
    def __init__(self):
        self.open=[]
        self.close=[]
        self.opstr,self.clstr='',''

    def push(self,x=None,y=None):
        if x==None:
            pass
        else:
            self.open.append(x)
        if y==None:
            pass
        else:
            self.close.append(y)

    def pop(self):
        for i,op in enumerate(self.open):
            for j,cl in enumerate(self.close):
                if op=='(' and cl==')':
                    self.open[i]=0
                    self.close[j]=0
                    break
                if op=='[' and cl==']':
                    self.open[i]=0
                    self.close[j]=0
                    break
                if op=='{' and cl=='}':
                    self.open[i]=0
                    self.close[j]=0
                    break
                
        while 0 in self.open and 0 in self.close:
            self.open.remove(0)
            self.close.remove(0)
        
        for i in self.open:
            self.opstr+=i
        for i in self.close:
            self.clstr+=i

    def peek(self):
        if len(self.open)==0 and len(self.close)==0:
            return 'MATCH'
        if len(self.open)==0 and len(self.close)!=0:
            return 'close paren excess'
        if len(self.open)!=0 and len(self.close)==0:
            return f'open paren excess   {len(self.open)} : {self.opstr}'
        else:
            return 'Unmatch open-close'


s=Stack()
inp=input('Enter expresion : ')

for i in inp:
    if i in '([{':
        s.push(i,None)
    if i in ')]}':
        s.push(None,i)

s.pop()
print(inp,s.peek())