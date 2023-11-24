def bfs(arr, start):
    a = [start]
    b = {start: 0}
    i = 0
    while i < len(a):
        for x in arr[a[i]]:
            if x not in a:
                a.append(x)
                b[x] = b[a[i]] + 1

        i += 1

    return b


arr = [
    [],
    [2, 3, 4],
    [1],
    [1, 7, 8],
    [1, 5, 6],
    [4],
    [4, 8],
    [3, 8],
    [3, 6, 7]
]

mp = bfs(arr, 1)
for i in sorted(mp):
    print(f'{i}: {mp[i]}')
