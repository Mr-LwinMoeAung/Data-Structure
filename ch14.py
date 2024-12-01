#  *** Data type integer float string ***
# Enter a word : 1.2345
#  === Float Mode ===
# 1.23450 = 1 + 0.23450
# Sum of 2 decimal point digits = 2 + 3 = 5
# 1.234500 = 1.23449999999999993072


print(' *** Data type integer float string ***')
inp=input('Enter a word : ')

try:
    inp=int(inp)
    print(' === Integer Mode ===')
    print(f'{inp:,} * 2 = {(inp*2):,}')
    print(f'{inp:,} tenth digit = {inp//10%10}')
    print(f'{inp:,} base 16 = {inp:X}')
    print(f'{inp:,} right 8-digit binary = {inp//16%16:04b} {inp%16:04b}')

except:
    try:
        inp=float(inp)
        print(' === Float Mode ===')
        div=int(inp)
        b=inp%div
        print(f'{inp:.5f} = {div} + {b:.5f}')
        c=int(b*10)
        d=int(b*100)
        d=d%10
        print(f'Sum of 2 decimal point digits = {c} + {d} = {c+d}')
        print(f'{inp:.6f} = {inp:.20f}')
    except:
        print(' === String Mode ===')
        print(f'{inp} {inp*2} {inp*3}')