t = int(input())

for i in range(t):
    n = int(input())
    lengths = []
    arr = list(map(int, input().split()))
    count = 0
    min_elem = arr[0]
    for j in range(n):
        if arr[j] < min_elem:
            min_elem = arr[j]
        count += 1
        if count > min_elem:
            lengths.append(count - 1)
            count = 1
            min_elem = arr[j]
        elif count == min_elem:
            lengths.append(count)
            count = 0
            if j < n - 1:
                min_elem = arr[j + 1]
            else:
                break
    if count > 0:
        lengths.append(count)

    print(len(lengths))
    print(' '.join([str(elem) for elem in lengths]))