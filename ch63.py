def generate_binary_subsets(n, current_subset=""):
    if n == 0:
        print(current_subset)
    else:
        generate_binary_subsets(n - 1, current_subset + "0")
        generate_binary_subsets(n - 1, current_subset + "1")

print(' *** Decimal to Binary Subsets Genterator ***')
n = int(input("Enter digit : "))

if n <= 0:
    print(f"{n} is NOT a valid input !!!")
else:
    generate_binary_subsets(n)