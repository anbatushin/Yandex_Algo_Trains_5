def LBinSearch(mas, left) -> int:
    l = 0
    r = len(mas)
    while l < r:
        med = (l + r) // 2
        if mas[med] < left:
            l = med + 1
        else:
            r = med
    return l


def RBinSearch(mas, right) -> int:
    l = 0
    r = len(mas)
    while l < r:
        med = (l + r) // 2
        if mas[med] <= right:
            l = med + 1
        else:
            r = med
    return l


if __name__ == '__main__':
    N = int(input())
    mas = sorted(list(map(int, input().split())))
    K = int(input())
    for _ in range(K):
        L, R = map(int, input().split())
        print(RBinSearch(mas, R) - LBinSearch(mas, L), end=' ')
