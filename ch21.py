#  *** integer summation from 1 to n ***
# Enter an integer(n) : 17
# Summation => 1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17 = 153

print(' *** integer summation from 1 to n ***')
inp=int(input('Enter an integer(n) : '))
sum=0

print('Summation => ',end='')

for i in range(1,inp+1):
    sum+=i
    print(i,end='')
    if i<inp:
        print('+',end='')

print(' =',sum)