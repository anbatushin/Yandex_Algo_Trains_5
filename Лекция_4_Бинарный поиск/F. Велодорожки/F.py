def MinPaths(w, h, n, coords) -> int:
    min_pref = [0] * (n + 2)
    max_pref = [0] * (n + 2)
    min_suf = [0] * (n + 2)
    max_suf = [0] * (n + 2)

    min_pref[1] = coords[1][1]
    max_pref[1] = coords[1][1]
    min_suf[n] = coords[n][1]
    max_suf[n] = coords[n][1]

    for i in range(n - 1, 0, -1):
        min_pref[n - i + 1] = min(min_pref[n - i], coords[n - i + 1][1])
        max_pref[n - i + 1] = max(max_pref[n - i], coords[n - i + 1][1])
        min_suf[i] = min(min_suf[i + 1], coords[i][1])
        max_suf[i] = max(max_suf[i + 1], coords[i][1])

    left = 1
    right = min(w, h)
    # min_med = max(maxx - minx, maxy - miny)
    min_med = min(w, h)
    # min_med = min(w, h)
    while left < right:
        med = (left + right) // 2
        fl = False
        '''
        # if med > maxx - minx:
            # continue
        fl = False
        l = 1
        while l + med - 1 < min(w, h) + 1:
            # print(l, med)
            # print(l + med - 1)
            # print(f'Pair: {l}, {l + med - 1}, med = {med}')
            x1 = cols[l - 1] + 1
            x2 = cols[l + med - 1]
            if x1 > 1 and x2 < n:
                # delta = max(max_pref[x1 - 1] - min_suf[x2 + 1], max_suf[x2 + 1] - min_pref[x1 - 1])
                delta = max(max_pref[x1 - 1], max_suf[x2 + 1]) - min(min_pref[x1 - 1], min_suf[x2 + 1])
                # print('do classic')
            elif x1 == 1 and x2 == n:
                delta = 0
                # print('delta = 0')
            elif x1 == 1:
                delta = max_suf[x2 + 1] - min_suf[x2 + 1]
                # print('do sufs')
            elif x2 == n:
                delta = max_pref[x1 - 1] - min_pref[x1 - 1]
                # print('do prefs')
            if delta + 1 <= med:
                fl = True
                # print(med, 'wins')
                break

            l += 1
        if fl:
            min_med = min(med, min_med)
            # print(f'Catch: {min_med} on {left} and {right}')
            right = med
        else:
            # print('Need more')
            left = med + 1
        '''
        index1 = 1
        index2 = 1
        while index2 <= n:
            if coords[index2][0] - coords[index1][0] >= med or index2 == n:
                if index2 == n:
                    x2 = n
                    x1 = index1
                    index2 += 1
                else:
                    # print(index1, index2)
                    x1 = index1
                    x2 = index2 - 1
                    # print(x1, x2)
                    while coords[index1][0] == coords[index1 + 1][0]:
                        index1 += 1
                    index1 += 1
                if x1 > 1 and x2 < n:
                    delta = max(max_pref[x1 - 1], max_suf[x2 + 1]) - min(min_pref[x1 - 1], min_suf[x2 + 1])
                elif x1 == 1 and x2 == n:
                    delta = 0
                elif x1 == 1:
                    delta = max_suf[x2 + 1] - min_suf[x2 + 1]
                elif x2 == n:
                    delta = max_pref[x1 - 1] - min_pref[x1 - 1]
                if delta + 1 <= med:
                    fl = True
                    break
            else:
                index2 += 1
        if fl:
            min_med = min(med, min_med)
            # print(f'check: {x1, x2}')
            right = med
        else:
            left = med + 1

    return min_med


if __name__ == '__main__':
    # width, height, N = map(int, input().split())
    f = open('input.txt', 'r')
    width, height, N = map(int, f.readline().split())
    coordinates = [] * (N + 1)
    coordinates.append([0, 0])
    for _ in range(N):
        # x, y = map(int, input().split())
        x, y = map(int, f.readline().split())
        if height < width:
            coordinates.append([y, x])
        else:
            coordinates.append([x, y])
    coordinates.sort()
    f.close()
    f = open('output.txt', 'w')
    # print(MinPaths(width, height, N, coordinates))
    f.write(str(MinPaths(width, height, N, coordinates)))
    f.close()
