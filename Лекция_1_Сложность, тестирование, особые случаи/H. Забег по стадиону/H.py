L, x1, v1, x2, v2 = map(int, input().split())

timelist = [0] * 4

if v1 == 0 and v2 == 0:
    if x1 == x2 or x1 == L - x2:
        print('yes')
        print(0.0)
    else:
        print('no')
elif v1 == 0 and v2 != 0:
    timelist[0] = (x1 - x2) / v2
    timelist[1] = (L - x1 - x2) / v2

    if timelist[0] < 0:
        mintime = timelist[1]
    else:
        if timelist[1] < 0:
            mintime = timelist[0]
        else:
            if timelist[0] < timelist[1]:
                mintime = timelist[0]
            else:
                mintime = timelist[1]
    print('yes')
    print(mintime)
elif v1 != 0 and v2 == 0:
    timelist[0] = (x2 - x1) / v1
    timelist[1] = (L - x1 - x2) / v1

    if timelist[0] < 0:
        mintime = timelist[1]
    else:
        if timelist[1] < 0:
            mintime = timelist[0]
        else:
            if timelist[0] < timelist[1]:
                mintime = timelist[0]
            else:
                mintime = timelist[1]
    print('yes')
    print(mintime)

elif v1 == v2:
    if x1 == x2 or x1 == L - x2:
        print('yes')
        print(0.0)

    else:
        timelist[0] = (- x2 - x1) / (2 * v1)
        timelist[1] = (L - x1 - x2) / (2 * v1)
        timelist[2] = (-L - x2 - x1) / (2 * v1)

        for i in range(3):
            if timelist[i] >= 0:
                mintime = timelist[i]
        for i in range(3):
            if 0 <= timelist[i] < mintime:
                mintime = timelist[i]

        print('yes')
        print(mintime)

elif v1 == -v2:
    if x1 == L - x2 or x1 == x2:
        print('yes')
        print(0.0)
    else:
        timelist[0] = (x1 - x2) / (v2 - v1)
        timelist[1] = (L + x2 - x1) / (v1 - v2)
        timelist[2] = (L - x1 + x2) / (v1 - v2)
    # print(timelist)

    for i in range(3):
        if timelist[i] >= 0:
            mintime = timelist[i]
    for i in range(3):
        if 0 <= timelist[i] < mintime:
            mintime = timelist[i]

    print('yes')
    print(mintime)

else:

    if v1 * v2 < 0:
        vabs = abs(v1) + abs(v2)
    if v1 * v2 > 0:
        vabs = max(abs(v2), abs(v1)) + min(abs(v2), abs(v1))

    timelist[0] = (x2 - x1) / (v1 - v2)
    timelist[1] = (L - x1 + x2) / (v1 - v2)
    timelist[2] = (-L - x1 + x2) / (v1 - v2)
    timelist[3] = (L - x1 - x2) / (v1 + v2)

    for i in range(4):
        if timelist[i] < 0:
            timelist[i] += L / vabs

    #    print (timelist)

    for i in range(4):
        if timelist[i] >= 0:
            mintime = timelist[i]
    for i in range(4):
        if 0 <= timelist[i] < mintime:
            mintime = timelist[i]

    print('yes')
    print(mintime)
# print (timelist)
