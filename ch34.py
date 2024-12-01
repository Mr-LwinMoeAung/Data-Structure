class Stack :

    def __init__(self):
        self.box,self.alpha,self.post,self.op=[],[],[],[]
        self.high=['*','/']
        self.low=['+','-']
        self.pa=['(',')']
        self.last=[]
    
    def compare(self,one,two):
        if one=='*' and two in '*/+-':
            return True
        if one=='/' and two in '*/+-':
            return True
        if one=='+' and two in '+-':
            return True
        if one=='-' and two in '+-':
            return True
        
    def push(self,ele):
        count=0
        for i in range(ord('a'),ord('z')+1):
            self.alpha.append(chr(i))
        for i in ele:
            self.box.append(i)
        for i,find in enumerate(self.box):
            count=0
            if find in self.alpha:
                self.post.append(find)
            else:
                self.op.append(find)
                if len(self.op)!=1:
                    for a in range(len(self.op)):
                        for b in range(len(self.op)):
                            if a<b: 
                                if self.op[a]=='(':
                                    if self.op[b]==')':
                                        between=self.op[a + 1:b]
                                        for i in between:
                                            self.post.append(i)
                                        self.op[a]='@'
                                        self.op[b]='@'
                                        for z in range(a+1,b):
                                                self.op[z]='@'     
                                    if self.op[b]=='(':
                                        if b-a>0:
                                            between=self.op[a + 1:b]
                                            for o in between:
                                                self.last.append(o)
                                            for z in range(a+1,b):
                                                self.op[z]='@'
                                            self.op[b]='@'
                                if self.compare(self.op[a],self.op[b]):
                                    count+=1
                                    self.post.append(self.op[a])
                                    if count==2:
                                        self.post.insert(len(self.post)-2,self.post[len(self.post)-1])
                                        self.post.pop(len(self.post)-1)
                                        count=0
                                    self.op[a]='@'
                while '@' in self.op:
                    self.op.remove('@')     
        if len(self.op)==2:
            if self.compare(self.op[0],self.op[1])!=True:
                self.op=self.op[::-1]
        self.post.extend(self.op)
        self.post.extend(self.last)
        while ')' in self.post:
            self.post.remove(')')
        return ''.join(self.post)

def infix2postfix(exp) :
    s = Stack()
    return s.push(exp)

print(" ***Infix to Postfix***")
token = input("Enter Infix expression : ")
print("PostFix => ",end='')
print(infix2postfix(token))