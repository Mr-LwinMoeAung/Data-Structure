print(' *** Triangle Checking ***')
user=input('Enter 3 sides : ')
x,y,z=user.split()
x=int(x)
y=int(y)
z=int(z)

if(x>0 and y>0 and z>0):
    if x>=y and x>=z:
        if y>z:
            print(f'max={x} mid={y} min={z}')
        elif z>y:
            print(f'max={x} mid={z} min={y}')
        else:
            print(f'max={x} mid={y} min={z}')
    if y>x and y>z:
        if x>z:
            print(f'max={y} mid={x} min={z}')
        elif z>x:
            print(f'max={y} mid={z} min={x}')
        else: 
            print(f'max={y} mid={x} min={z}')
    if z>x and z>y:
        if x>y:
            print(f'max={z} mid={x} min={y}')
        elif y>x:
            print(f'max={z} mid={y} min={x}')
        else:
            print(f'max={z} mid={x} min={y}')
    if (x>1 or y>1 or y>1) and (x==y!=z or x==z!=y or y==x!=z or y==z!=x or z==x!=y or z==y!=x):
        print(f'{x}, {y} and {z} are sides of ISOSCELES triangle.')
    elif x==y==z:
        print(f'{x}, {y} and {z} are sides of EQUIlATERAL triangle.')
    elif x!=y!=z!=x and (x-1!=y or y-1!=z):
        print(f'{x}, {y} and {z} are sides of RIGHT triangle.')
    elif x-1==y and y-1==z:
        print(f'{x}, {y} and {z} are sides of SCALENE triangle.')
    else:
        print(f'{x}, {y} and {z} are not side of triangle.')
else:
    print('Invalid input !!!')
    quit()