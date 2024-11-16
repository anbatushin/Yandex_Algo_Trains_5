n, k = map(int, input().split())

dct = {}
count = -1
exist = False
for elem in map(int, input().split()):
    count += 1
    if elem in dct:
        if count - dct[elem] <= k:
            exist = True
            break
    dct[elem] = count

print('YES' if exist else 'NO')
