from collections import Counter


n = int(input())
dct_arr = Counter(list(map(int, input().split())))
keys = sorted(list(dct_arr.keys()))
# print(dct_arr)
max_count = 0
if len(keys) <= 2:
    print(max_count)
else:
    for i in range(len(keys) - 1):
        if abs(keys[i] - keys[i + 1]) <= 1 and dct_arr[keys[i]] + dct_arr[keys[i + 1]] > max_count:
            max_count = dct_arr[keys[i]] + dct_arr[keys[i + 1]]
    if max_count == 0:
        max_count += 1
    print(n - max_count)
