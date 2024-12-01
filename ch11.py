print(' *** Circumfernce and Area Calculator ***')
inp=input('Enter radius : ')
pi=3.14159265853

try:
    inp=int(inp)
except:
    inp=float(inp)

Circumfernce = 2*pi*inp
area=pi*inp**2

print(f'Circumference = {Circumfernce:.3f}')
print(f'Area={area:.5f}')