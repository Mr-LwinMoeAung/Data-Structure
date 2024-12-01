print('*** multiplication or sum ***')
a,b=input('Enter num1 num2 : ').split()
a=int(a)
b=int(b)

check=a*b

if check<=1000:
    print('The result is',a*b)
else:
    print('The result is',a+b)