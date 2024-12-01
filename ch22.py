print(' *** Pyramid IV ***')
inp=int(input('Enter height : '))
start=ord('z')
count=0

for i in range(1,inp+1):
    ans=start-count
    for j in range(inp-i):
        print(' ',end='')
    for k in range(i):
        print(chr(ans),end='')
        if ans<=ord('a'):
            ans=ord('z')
            count=0
        else:
            ans-=1
            count+=1
    for x in range(i-1):
        print(chr(ans),end='')
        if ans<=ord('a'):
            ans=ord('z')
            count=0
        else:
            ans-=1
            count+=1
    print()

print('===== End of program =====')