n = int(input())
lst_plus = []
lst_minus = []
index = 0

max_b = 0
max_a = 0
for i in range(n):
    a, b = map(int, input().split())
    if a - b >= 0:
        if max_b < b:
            max_b = b
            lst_plus.append([a, b, i + 1])
        else:
            lst_plus.append([a, b, i + 1])
            if len(lst_plus) >= 2:
                lst_plus[-2], lst_plus[-1] = lst_plus[-1], lst_plus[-2]
    else:
        if max_a < a:
            max_a = a
            lst_minus.append([a, b, i + 1])
        else:
            lst_minus.append([a, b, i + 1])
            if len(lst_minus) >= 2:
                lst_minus[-2], lst_minus[-1] = lst_minus[-1], lst_minus[-2]

sum = 0
max_sum = 0
for i in range(len(lst_plus)):
    sum += lst_plus[i][0]
    if max_sum < sum:
        max_sum = sum
    sum -= lst_plus[i][1]
# print(lst_plus)
if len(lst_minus) > 0:
    sum += lst_minus[-1][0]
    if max_sum < sum:
        max_sum = sum
# print(lst_minus)
print(max_sum)

for i in range(len(lst_plus)):
    print(lst_plus[i][2], end=' ')
for i in range(len(lst_minus) - 1, -1, -1):
    print(lst_minus[i][2], end=' ')
