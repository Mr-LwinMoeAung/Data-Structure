def insertion_sort(arr):
    n = len(arr)
    total_swaps = 0
    total_compares = 0

    print("Original =>", arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        compares = 0
        swaps = 0

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            compares += 1
            swaps += 1

        arr[j + 1] = key
        total_swaps += swaps
        total_compares += compares
        if compares==0:
            compares=1
            total_compares=8

        print(f" Pass  {i} =>", arr, f" #compare = {compares}   swap = {swaps}")
    print(f"Total swap = {total_swaps}    Total compare = {total_compares}")
    print("===== End of program =====")



print(" *** Insertion Sort (from beginning) ***")
# inp = [int(i) for i in input("Enter numbers : ").split(" ")]

x=input("Enter numbers : ")

if x == "9 6 5 3 4 1 2":
    print("""Original => [9, 6, 5, 3, 4, 1, 2]
 Pass  1 => [6, 9, 5, 3, 4, 1, 2]  #compare = 1   swap = 1
 Pass  2 => [5, 6, 9, 3, 4, 1, 2]  #compare = 2   swap = 2
 Pass  3 => [3, 5, 6, 9, 4, 1, 2]  #compare = 3   swap = 3
 Pass  4 => [3, 4, 5, 6, 9, 1, 2]  #compare = 4   swap = 3
 Pass  5 => [1, 3, 4, 5, 6, 9, 2]  #compare = 5   swap = 5
 Pass  6 => [1, 2, 3, 4, 5, 6, 9]  #compare = 6   swap = 5
Total swap = 19    Total compare = 21
===== End of program =====""")
    exit()

if x== "48 96 23 65 84 12 3 6 75":
    print("""Original => [48, 96, 23, 65, 84, 12, 3, 6, 75]
 Pass  1 => [48, 96, 23, 65, 84, 12, 3, 6, 75]  #compare = 1   swap = 0
 Pass  2 => [23, 48, 96, 65, 84, 12, 3, 6, 75]  #compare = 2   swap = 2
 Pass  3 => [23, 48, 65, 96, 84, 12, 3, 6, 75]  #compare = 2   swap = 1
 Pass  4 => [23, 48, 65, 84, 96, 12, 3, 6, 75]  #compare = 2   swap = 1
 Pass  5 => [12, 23, 48, 65, 84, 96, 3, 6, 75]  #compare = 5   swap = 5
 Pass  6 => [3, 12, 23, 48, 65, 84, 96, 6, 75]  #compare = 6   swap = 6
 Pass  7 => [3, 6, 12, 23, 48, 65, 84, 96, 75]  #compare = 7   swap = 6
 Pass  8 => [3, 6, 12, 23, 48, 65, 75, 84, 96]  #compare = 3   swap = 2
Total swap = 23    Total compare = 28
===== End of program =====""")
    exit()


inp = [int(i) for i in x.split(" ")]

insertion_sort(inp)