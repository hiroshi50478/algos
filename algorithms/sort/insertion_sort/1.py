def insertion_sort(arr):
    for i in range(1, len(arr)):
        x = arr[i]
        j = i - 1
        while (j >= 0 and arr[j] > x):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = x
    return arr


arr = [1, -1, 3, 9, 0, 0, 4, 2, -5]
arr = insertion_sort(arr)
print(arr)
