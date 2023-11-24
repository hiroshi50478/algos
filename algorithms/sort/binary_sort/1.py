def binary_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    mid = int(length / 2)
    mid = arr.pop(mid)
    left, right = [], []
    for x in arr:
        if x <= mid:
            left.append(x)
        else:
            right.append(x)

    return binary_sort(left) + [mid] + binary_sort(right)


arr = [1, -1, 3, 9, 0, 0, 4, 2, -5]
arr = binary_sort(arr)
print(arr)
