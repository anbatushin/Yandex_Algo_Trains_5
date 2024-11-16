def SquareCoords(coords, n) -> set:
    res = set()
    min_count = 3
    if n == 1:
        for [x_coord, y_coord] in coords:
            # res.add((x_coord, y_coord))
            res.add((x_coord - 1, y_coord))
            res.add((x_coord, y_coord - 1))
            res.add((x_coord - 1, y_coord - 1))
    else:
        for first_pair in coords:
            for second_pair in coords:
                if first_pair != second_pair:
                    x1 = first_pair[0]
                    y1 = first_pair[1]
                    x2 = second_pair[0]
                    y2 = second_pair[1]
                    c1 = (x2 - (y2 - y1), y2 + (x2 - x1))
                    d1 = (x1 - (y2 - y1), y1 + (x2 - x1))
                    c2 = (x2 + (y2 - y1), y2 - (x2 - x1))
                    d2 = (x1 + (y2 - y1), y1 - (x2 - x1))
                    if c1 in coords and d1 in coords:
                        res.clear()
                        # res.add(first_pair)
                        # res.add(second_pair)
                        # res.add(c1)
                        # res.add(d1)
                        print(0)
                        return res
                    elif c1 in coords or d1 in coords:
                        if min_count > 1:
                            res.clear()
                            min_count = 1
                        # res.add(first_pair)
                        # res.add(second_pair)
                            if c1 in coords:
                                res.add(d1)
                            else:
                                res.add(c1)
                    elif c2 in coords and d2 in coords:
                        res.clear()
                        # res.add(first_pair)
                        # res.add(second_pair)
                        # res.add(c2)
                        # res.add(d2)
                        print(0)
                        return res
                    elif c2 in coords or d2 in coords:
                        if min_count > 1:
                            res.clear()
                            min_count = 1
                        # res.add(first_pair)
                        # res.add(second_pair)
                            if c2 in coords:
                                res.add(d2)
                            else:
                                res.add(c2)
                    else:
                        if min_count == 3:
                            # res.add(first_pair)
                            # res.add(second_pair)
                            res.add(c1)
                            res.add(d1)
                            min_count = 2
    print(min_count)
    return res


if __name__ == '__main__':
    N = int(input())
    coordinates = set()
    for i in range(N):
        coordinates.add(tuple(map(int, input().split())))
    for x, y in SquareCoords(coordinates, N):
        print(x, y)
