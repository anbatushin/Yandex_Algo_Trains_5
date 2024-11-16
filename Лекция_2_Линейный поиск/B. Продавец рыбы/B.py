n, k = map(int, input().split())
arr = list(map(int, input().split()))

delta = 0
for i in range(n):
    for j in range(i + 1, min(i + k + 1, n)):
        if arr[j] - arr[i] > delta:
            delta = arr[j] - arr[i]

print(delta)
