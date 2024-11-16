x = int(input())
y = int(input())
p = int(input())


def Counter(a, b):
    res = 0
    # print(a, b)
    if b == 0:
        return 1
    while True:
        b -= a
        a -= b
        res += 1
        if a <= 0 < b:
            return -1
        elif b <= 0:
            # print(res)
            return res


def Count(x, y, p):
    # print(x, y, p)
    min = y + p
    if y + p <= x:
        return 1
    res = 0
    while True:
        if y + p <= x:
            res += 1
            if min <= res:
                return min
            else:
                return res
        # print(res, y)
        if y > x:
            res += 1
            y -= x - p
        else:
            tmpsum = Counter(x - (p - (x - y)), (p - (x - y)))
            res += 1
            if tmpsum != -1:
                res += tmpsum
                # print(res, 'd')
                if min >= res:
                    min = res
                res -= tmpsum
                y -= x - p
            else:
                y -= x - p
        if y <= 0:
            # print(res, 'l')
            # print(min)
            return min


sum = 0
if p > x:
    if y <= x:
        sum += 1
        print(sum)
    else:
        sum += 1
        if y - x >= x:
            print(-1)
        else:
            sum += 1
            subsum = Counter(x - (p - (x - (y - x))), p - (x - (y - x)))
            if subsum != -1:
                sum += subsum
                print(sum)
            else:
                print(-1)
elif p < x:
    sum += 1
    if y <= x:
        print(sum)
    else:
        # print(x - (p - (x - y)), (p - (x - y)))
        subsum = Count(x, y-x, p)
        if subsum != -1:
            sum += subsum
            print(sum)
        else:
            print(-1)
else:
    if y <= x:
        sum += 1
        print(sum)
    elif y - x < x:
        sum += 2
        subsum = Counter(x - (y - x), y - x)
        if subsum != -1:
            sum += subsum
            print(sum)
        else:
            print(-1)
    else:
        print(-1)
