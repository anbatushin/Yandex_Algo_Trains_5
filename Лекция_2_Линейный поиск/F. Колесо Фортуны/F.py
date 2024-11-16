n = int(input())
sectors = list(map(int, input().split()))
a, b, k = map(int, input().split())

if a % k == 0:
    pos_a = (a // k - 1) % n
else:
    pos_a = a // k % n

if b % k == 0:
    pos_b = (b // k - 1) % n
else:
    pos_b = b // k % n

if b - a >= n * k:
    print(max(sectors))
elif pos_a == pos_b:
    # print(pos_a, pos_b)
    print(max(sectors[pos_a], sectors[(n - pos_a) % n]))
elif pos_a < pos_b:
    maxwin = sectors[pos_b]
    for i in range(pos_a, pos_b):
        if sectors[i] > maxwin:
            maxwin = sectors[i]
    winmax = sectors[(n - pos_a) % n]
    for i in range(n - pos_b, n - pos_a):
        if sectors[i] > winmax:
            winmax = sectors[i]
    print(max(maxwin, winmax))
elif pos_a > pos_b:
    # print('lol', pos_a, pos_b)
    maxwin = sectors[pos_b]
    for i in range(pos_a, n):
        if sectors[i] > maxwin:
            maxwin = sectors[i]
    for i in range(pos_b):
        if sectors[i] > maxwin:
            maxwin = sectors[i]
    winmax = sectors[0]
    if pos_b == 0:
        for i in range(n - pos_a):
            if sectors[i] > winmax:
                winmax = sectors[i]
    else:
        for i in range((n - pos_b + 1) % n, n):
            if sectors[i] > winmax:
                winmax = sectors[i]
        for i in range((n - pos_a + 1) % n):
            if sectors[i] > winmax:
                winmax = sectors[i]
    # print(maxwin, winmax)
    print(max(maxwin, winmax))
