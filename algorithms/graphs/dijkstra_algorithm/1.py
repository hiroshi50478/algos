def dijkstra_algorithm(matrix, start):
    a = [float('inf') for _ in range(len(matrix))]
    a[start - 1] = 0
    for i in range(len(a)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < 0:
                continue
            a[j] = min(a[j], a[i] + matrix[i][j])

    return a


matrix = [[-1, 2, 1, -1, -1, -1],
          [2, -1, 1, 4, 5, -1],
          [1, 1, -1, 4, 6, -1],
          [-1, 4, 4, -1, 2, 6],
          [-1, 5, 6, 2, -1, 3],
          [-1, -1, -1, 6, 3, -1]]
print(dijkstra_algorithm(matrix, 1))