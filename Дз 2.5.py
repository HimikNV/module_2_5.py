def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
matrix1 = get_matrix(2, 2, 10)
matrix2 = get_matrix(3, 5, 42)
matrix3 = get_matrix(4, 2, 13)



