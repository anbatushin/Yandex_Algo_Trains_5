def Fraction(n) -> None:
    left = 1
    right = n
    while left < right:
        med = (left + right) // 2
        if med * (med + 1) // 2 < n:
            left = med + 1
        else:
            right = med
    if left % 2 == 1:
        up = n - left * (left - 1) // 2
        down = left - up + 1
    else:
        down = n - left * (left - 1) // 2
        up = left - down + 1
    print(f'{up}/{down}')
    return


if __name__ == '__main__':
    N = int(input())
    Fraction(N)
