def PrefBin(pref_sum, l, s) -> int:
    left = 0
    right = len(arr) - l + 1
    while left < right:
        med = (left + right) // 2
        if pref_sum[med + l] - pref_sum[med] == s:
            return med
        elif pref_sum[med + l] - pref_sum[med] < s:
            left = med + 1
        else:
            right = med
    return -1


if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    pref_sum = [0] * (len(arr) + 1)
    pref_sum[1] = arr[0]
    for i in range(1, len(arr)):
        pref_sum[i + 1] = pref_sum[i] + arr[i]

    file = open('output.txt', 'w')

    for _ in range(M):
        l, s = map(int, input().split())
        result = PrefBin(pref_sum, l, s)
        if result == -1:
            file.write(str(-1) + '\n')
        else:
            file.write(str(result + 1) + '\n')
    file.close()
