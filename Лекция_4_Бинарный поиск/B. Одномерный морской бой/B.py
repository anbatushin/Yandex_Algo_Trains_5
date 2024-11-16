def RBinSearch(n) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    l = 0
    r = n
    while l < r:
        med = (l + r) // 2
        f = lambda k: (k ** 3 + 6 * k ** 2 + 5 * k - 6) // 6
        # print(func(med))
        if f(med) <= n:
            l = med + 1
        else:
            r = med
    return l - 1


if __name__ == '__main__':
    n = int(input())
    print(RBinSearch(n))
