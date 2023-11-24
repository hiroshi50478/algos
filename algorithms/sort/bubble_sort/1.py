def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


arr = [1, -1, 3, 9, 0, 0, 4, 2, -5]
arr = bubble_sort(arr)
print(arr)
