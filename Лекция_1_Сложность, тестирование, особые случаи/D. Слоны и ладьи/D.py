def RChange(i, j):
    if i != 0:
        for p in range(i, -1, -1):
            if p == i:
                continue
            match chess[p][j]:
                case '*':
                    chess[p][j] = 'X'
                case 'X':
                    continue
                case 'R':
                    break
                case 'B':
                    break

    if i != 7:
        for p in range(i, 8):
            if p == i:
                continue
            match chess[p][j]:
                case '*':
                    chess[p][j] = 'X'
                case 'X':
                    continue
                case 'R':
                    break
                case 'B':
                    break

    if j != 0:
        for q in range(j, -1, -1):
            if q == j:
                continue
            match chess[i][q]:
                case '*':
                    chess[i][q] = 'X'
                case 'X':
                    continue
                case 'R':
                    break
                case 'B':
                    break

    if j != 7:
        for q in range(j, 8):
            if q == j:
                continue
            match chess[i][q]:
                case '*':
                    chess[i][q] = 'X'
                case 'X':
                    continue
                case 'R':
                    break
                case 'B':
                    break


def BChange(i, j):
    if i != 0 and j != 0:
        a = 1
        while i - a >= 0 and j - a >= 0:
            match chess[i - a][j - a]:
                case '*':
                    chess[i - a][j - a] = 'X'
                case 'X':
                    a += 1
                    continue
                case 'R':
                    break
                case 'B':
                    break
            a += 1

    if i != 0 and j != 7:
        a = 1
        while i - a >= 0 and j + a <= 7:
            match chess[i - a][j + a]:
                case '*':
                    chess[i - a][j + a] = 'X'
                case 'X':
                    a += 1
                    continue
                case 'R':
                    break
                case 'B':
                    break
            a += 1

    if i != 7 and j != 7:
        a = 1
        while i + a <= 7 and j + a <= 7:
            match chess[i + a][j + a]:
                case '*':
                    chess[i + a][j + a] = 'X'
                case 'X':
                    a += 1
                    continue
                case 'R':
                    break
                case 'B':
                    break
            a += 1

    if i != 7 and j != 0:
        a = 1
        while i + a <= 7 and j - a >= 0:
            match chess[i + a][j - a]:
                case '*':
                    chess[i + a][j - a] = 'X'
                case 'X':
                    a += 1
                    continue
                case 'R':
                    break
                case 'B':
                    break
            a += 1


chess = []
for i in range(8):
    s = list(input())
    chess.append(s[:8])

for i in range(8):
    for j in range(8):
        match chess[i][j]:
            case '*':
                continue
            case 'X':
                continue
            case 'R':
                RChange(i, j)
            case 'B':
                BChange(i, j)

sum = 0
for i in range(8):
    for j in range(8):
        if chess[i][j] == '*':
            sum += 1

print(sum)
