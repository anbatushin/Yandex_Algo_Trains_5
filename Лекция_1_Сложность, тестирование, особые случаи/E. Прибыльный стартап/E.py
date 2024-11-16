n, k, d = map(int, input().split())

for i in range(10):
    if (n * 10 + i) % k != 0:
        if i == 9:
            print(-1)
    else:
        print(str(n) + str(i) + '0' * (d - 1))
        break
