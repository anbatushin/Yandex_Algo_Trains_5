m, n = map(int, input().split())

# matrix = [[0] * (n + 1) for i in range(m)]
matrix = []
for i in range(m):
    matrix.append([symbol for symbol in input()])
    matrix[i].append('*')

# print(matrix)

a_flag = False
b_flag = False
error_flag = False
x = -1
count = 0
ha = 0
xa = 0
ya = 0
prop = 0
for i in range(m):
    h = m + 1
    for j in range(n + 1):
        # print(i, h, ya, ha, matrix[i][j])
        if matrix[i][j] == '#' or m + 1 > h == (ha - (i - ya)) and matrix[i][j] == 'a':
            # print('lol')
            if h == m + 1:
                x = j
            k = 1
            while i + k <= m - 1 and (matrix[i + k][j] == '#' or matrix == 'a'):
                k += 1
            # print(k, h, 'lol')
            if k - 1 < h:
                h = k - 1
        else:
            if m + 1 > h != (ha - (i - ya)) and matrix[i][j] == 'a':
                prop += 1
        # print(x, h)
        # print(matrix[i][j], i, j, h)
        if matrix[i][j] != 'a' and matrix[i][j] != '#' and (
                x != -1 or (j == n and i == m - 1 and x != -1) or j == n and x != -1):
            # print('change')
            for t in range(x, j - prop):
                for p in range(i, i + h + 1):
                    if not a_flag:
                        # print(p, t, matrix[p][t])
                        matrix[p][t] = 'a'
                    elif not b_flag:
                        # print(t, x, h, xa, ha)
                        if (ha - (i - ya)) == h or t < xa or matrix[p][t] != 'a':
                            # print(t, xa)
                            matrix[p][t] = 'b'
                    else:
                        error_flag = True
                        break
            count = (j - x) * (h + 1)
            last_i1 = i
            last_j1 = x
            last_i2 = i + h
            last_j2 = j - 1 - prop
            if not a_flag:
                a_flag = True
                ha = h
                xa = x
                ya = i
            elif not b_flag:
                b_flag = True
            h = m + 1
            x = -1
            prop = 0
    if error_flag:
        # print('NO')
        break

    else:
        matrix[i].pop()
    """
        print('------------')
        for s in matrix:
            print(' '.join(list(s)))
        print('------------')
    """
# print(matrix)

if not a_flag:
    error_flag = True

if a_flag == True and b_flag == False and count > 1:
    if last_i2 > last_i1:
        for j in range(last_j1, last_j2 + 1):
            matrix[last_i2][j] = 'b'
    else:
        matrix[last_i2][last_j2] = 'b'
    b_flag = True

# print(error_flag, a_flag, b_flag)
if error_flag == True or a_flag == True and b_flag == False and count == 1:
    print('NO')
else:
    print('YES')
    # print('------------')
    for s in matrix:
        print(''.join(list(s)))
    # print('------------')
