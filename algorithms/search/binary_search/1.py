def binary_search(arr, key):
    x = int(len(arr) / 2)
    i = x
    while arr[i] != key:
        x = int(x / 2)
        if key < arr[i]:
            i -= max(x, 1)
        else:
            i += max(x, 1)
    return i


a = [1, -1, 3, 9, 0, 0, 4, 2, -5]
a.sort()
x = 9
print(binary_search(a, x))
