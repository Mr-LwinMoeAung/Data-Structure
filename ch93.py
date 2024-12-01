def insertion_sort_gap(inp, start, gap, total_swaps):
    for i in range(start + gap, len(inp), gap):
        value = inp[i]
        j = i
        while j >= gap and inp[j - gap] > value:
            inp[j] = inp[j - gap]
            j -= gap
            total_swaps += 1
        inp[j] = value
    return total_swaps

def shell_sort(shell_sort_list, inc):
    total_swaps = 0
    for gap in inc:
        for i in range(gap):
            total_swaps = insertion_sort_gap(shell_sort_list, i, gap, total_swaps)
        print(f"inc={gap} => {shell_sort_list}")
    return total_swaps

print(" *** Shell Sort ***")
inp, incSequence = input("Enter numbers / incremental sequence : ").split('/')
inpList = inp.split()
myList = [int(ele) for ele in inpList]
incSequence = [int(ele) for ele in incSequence.split()]
print(f"Original => {myList}")
print(f"incSequence => {incSequence}")
shell_sort_list = myList[:]
total_swap = shell_sort(shell_sort_list, incSequence[::-1])
print(f"Shell sort Total swap = {total_swap}")

def insertion_sort(inp):
    total_swaps = 0
    for i in range(1, len(inp)):
        key = inp[i]
        j = i - 1
        while j >=0 and key < inp[j]:
            inp[j+1] = inp[j]
            j -= 1
            total_swaps += 1
        inp[j+1] = key
    return total_swaps

i_sort_list = list(myList)
print(f"insertion before => {i_sort_list}")
total_swap = insertion_sort(i_sort_list)
print(f"insertion afer   => {i_sort_list}")
print(f"Insertion sort total swap = {total_swap}")

print("===== End of program =====")
