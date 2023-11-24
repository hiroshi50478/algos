def selection_sort(a):
    for i in range(len(arr) - 1):
        _i = i
        for j in range(i + 1, len(arr)):
            if (arr[j] < arr[_i]):
                _i = j
        arr[_i], arr[i] = arr[i], arr[_i]
    return arr


arr = [1, -1, 3, 9, 0, 0, 4, 2, -5]
arr = selection_sort(arr)
print(arr)
