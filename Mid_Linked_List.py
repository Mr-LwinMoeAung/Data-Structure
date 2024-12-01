row= 5

for i in range(row):
    for j in range(row-i-1):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    for j in range(i):
        print('*',end='')
    print()