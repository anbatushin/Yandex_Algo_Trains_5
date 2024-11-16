n = int(input())

sum = 0
for i in range(n):
    a = int(input())
    if a % 4 == 1:
        sum += a // 4 + 1
    elif a % 4 == 0:
        sum += a // 4
    else:
        sum += a // 4 + 2

print(sum)
