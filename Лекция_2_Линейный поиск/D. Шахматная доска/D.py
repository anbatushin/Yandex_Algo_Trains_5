n = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
chess = []

for i in range(10):
    chess.append([1] * 10)

for i in range(n):
    x, y = map(int, input().split())
    chess[x][y] = 0

perim = 0
for i in range(1, 9):
    for j in range(1, 9):
        if chess[i][j] == 0:
            for k in range(len(dx)):
                perim += chess[i + dx[k]][j + dy[k]]

print(perim)
