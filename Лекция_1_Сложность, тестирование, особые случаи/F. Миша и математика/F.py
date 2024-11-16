n = int(input())
s = list(map(int, input().split()))

fl = s[0] % 2
count = fl
for i in range(1, n):
    if s[i] % 2 == 1:
        count += 1
    if fl == 1 and s[i] % 2 == 1 or fl == 0 and count % 2 == 0:
        if fl == 0 and count > 0:
            count -= 1
        if fl == 1:
            count -= 1
        print('x', end='')
    else:
        print('+', end='')
    fl = s[i] % 2

