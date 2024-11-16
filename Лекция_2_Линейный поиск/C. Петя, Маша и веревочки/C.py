n = int(input())
arr = list(map(int, input().split()))

sum = 0
max_length = 0

for i in range(n):
    if arr[i] > max_length:
        sum += max_length
        max_length = arr[i]
    else:
        sum += arr[i]

if max_length <= sum:
    min_rope = max_length + sum
else:
    min_rope = max_length - sum

print(min_rope)
