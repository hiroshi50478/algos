def merge(a, b):
    ia, ib = 0, 0
    la, lb = len(a), len(b)
    c = []
    while ia < la and ib < lb:
        if a[ia] < b[ib]:
            c.append(a[ia])
            ia += 1
        else:
            c.append(b[ib])
            ib += 1
    if ia < la:
        c += a[ia:]
    if ib < lb:
        c += b[ib:]
    return c


def merge_sort(a):
    arr = []
    length = len(a)
    for i in range(0, length - 1, 2):
        if a[i + 1] > a[i]:
            arr.append([a[i], a[i + 1]])
        else:
            arr.append([a[i + 1], a[i]])
    if length % 2 == 1:
        arr.append([a[-1]])

    i = 0
    _arr = []
    while len(arr) != 1:
        _arr.append(merge(arr[i], arr[i + 1]))
        i += 2

        if i >= len(arr) - 1:
            if len(arr) % 2 == 1:
                _arr.append(arr[-1])
            i = 0
            arr = [*_arr]
            _arr = []

    return arr[0]


arr = [1, -1, 3, 9, 0, 0, 4, 2, -5]
arr = merge_sort(arr)
print(arr)
