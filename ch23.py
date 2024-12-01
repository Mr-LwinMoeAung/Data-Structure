print(' *** Digit count and Summation ***')
inp=input('Enter an integer : ')
com,sum,box=int(inp),0,[]
print(f'number = {com:,}')

for i in str(com):
    box.append(int(i))

print('Total digits are: ',len(box))

for i in box:
    sum+=i
print('Summation =',sum)