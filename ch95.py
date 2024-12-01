def quicksort(arr, low, high, comparisons):
    if low < high:
        pivot_index, comparisons = partition(arr, low, high, comparisons)
        comparisons = quicksort(arr, low, pivot_index - 1, comparisons)
        comparisons = quicksort(arr, pivot_index + 1, high, comparisons)
    return comparisons

def partition(arr, low, high, comparisons):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1, comparisons

print(" *** Quick Sort ***")
inp = list(map(int, input("Enter numbers : ").split()))
comparisons = quicksort(inp, 0, len(inp) - 1, 0)
print(f"Sorted array = {inp}")
print(f"Number of comparisons = {comparisons}")
print("===== End of  program =====")