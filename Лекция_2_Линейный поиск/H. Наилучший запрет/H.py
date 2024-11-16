def MaxMatrix(matrix, n, m):
    max_elem = 0
    line, column = -1, -1
    for i in range(n):
        for j in range(m):
            if matrix[i][j] > max_elem:
                max_elem = matrix[i][j]
                line = i
                column = j
    return max_elem, line, column


n, m = map(int, input().split())

matrix = []
matrix_copy = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
# print(matrix)
for i in range(n):
    matrix_copy.append(matrix[i].copy())

max_element, max_line, max_column = MaxMatrix(matrix, n, m)
for j in range(m):
    matrix[max_line][j] = 0
for i in range(n):
    matrix_copy[i][max_column] = 0
# print(matrix, matrix_copy)

max_element, max_line2, max_column2 = MaxMatrix(matrix, n, m)
# print(max_element, max_line2, max_column2)
for i in range(n):
    matrix[i][max_column2] = 0
max1, line1, column1 = MaxMatrix(matrix, n, m)

max_element, max_line3, max_column3 = MaxMatrix(matrix_copy, n, m)
# print(max_element, max_line3, max_column3)
for j in range(m):
    matrix_copy[max_line3][j] = 0
max2, line2, column2 = MaxMatrix(matrix_copy, n, m)

if max1 > max2:
    print(max_line3 + 1, max_column + 1)
else:
    print(max_line + 1, max_column2 + 1)
