def SortShips(arr, count):
    for i in range(count):
        for j in range(count - i - 1):
            if arr[j][0] > arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


n = int(input())
ships = []
for i in range(n):
    ships.append(list(map(int, input().split())))

SortShips(ships, n)
# print(ships)
sum = 0
for i in range(n):
    sum += abs(ships[i][0] - (i + 1))

sum_column = [0] * n
for i in range(n):
    for j in range(n):
        sum_column[j] += abs(ships[i][1] - (j + 1))

min_sum = sum_column[0]
for i in range(n):
    if sum_column[i] < min_sum:
        min_sum = sum_column[i]

# print(columns)
# print(sum_column)
# print(sum, min_sum)
print(sum + min_sum)
