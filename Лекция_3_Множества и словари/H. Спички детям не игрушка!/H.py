def MaxMatches(coords_A, coords_B) -> int:
    delta = {}
    max_count = 0
    for pairs_A in coords_A.copy():
        fl = False
        for pairs_B in coords_B:
            dx = pairs_B[2] - pairs_A[2]
            dy = pairs_B[3] - pairs_A[3]
            if dx == pairs_B[0] - pairs_A[0] and dy == pairs_B[1] - pairs_A[1]:
                if (dx, dy) in delta:
                    delta[(dx, dy)] += 1
                else:
                    delta[(dx, dy)] = 1
                fl = True
                if max_count < delta[(dx, dy)]:
                    max_count = delta[(dx, dy)]
        if not fl:
            coords_A.remove(pairs_A)
    '''
    for dxdy in delta:
        for pairs_A in coords_A:
            if (pairs_A[0] + dxdy[0], pairs_A[1] + dxdy[1], pairs_A[2] + dxdy[0], pairs_A[3] + dxdy[1]) in coords_B:
                delta[dxdy] += 1
        max_count = max(max_count, delta[dxdy])
        # max_count = max(delta.values())
    # print(delta)
    '''

    return max_count


if __name__ == '__main__':
    N = int(input())
    matches_A = set()
    matches_B = set()
    for i in range(N):
        coords = list(map(int, input().split()))
        if coords[0] > coords[2] or coords[0] == coords[2] and coords[1] > coords[3]:
            coords[0], coords[2] = coords[2], coords[0]
            coords[1], coords[3] = coords[3], coords[1]
        matches_A.add(tuple(coords))
    for i in range(N):
        coords = list(map(int, input().split()))
        if coords[0] > coords[2] or coords[0] == coords[2] and coords[1] > coords[3]:
            coords[0], coords[2] = coords[2], coords[0]
            coords[1], coords[3] = coords[3], coords[1]
        matches_B.add(tuple(coords))

    # print(matches_A)
    # print(matches_B)

    print(N - MaxMatches(matches_A, matches_B))
