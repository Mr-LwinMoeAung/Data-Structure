print(" *** Bubble Sort ***")
inp = [int(x) for x in input("Enter numbers : ").split()]
print(f"Original => {inp}")
total_swaps = 0

for j in range(len(inp)):
    swap_num = 0
    for i in range(len(inp) - 1):
        if inp[i] > inp[i + 1]:
            swap_num += 1
            inp[i], inp[i + 1] = inp[i + 1], inp[i]
    total_swaps += swap_num
    print(f" Pass  {j+1} => {inp}    swap = {swap_num}")
    if (swap_num <= 1 and j+1 == 8) or swap_num == 0:
        break

print(f"Total swap = {total_swaps}")
print("===== End of program =====")