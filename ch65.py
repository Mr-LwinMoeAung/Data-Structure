def staircase(n, a=1):
    if a <= n:
        print("_" * (n - a) + "#" * a)
        return staircase(n, a + 1)
    else:
        return ""

print(" *** Staircase ***")
n = input("Enter Input : ")
n = int(n)
staircase(n)