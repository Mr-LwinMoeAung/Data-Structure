def fac(num):
    if num<=1:
        return num
    return fac(num-1)+fac(num-2)


inp=int(input('Enter Number : '))
print(f'fibo({inp}) = {fac(inp)}')