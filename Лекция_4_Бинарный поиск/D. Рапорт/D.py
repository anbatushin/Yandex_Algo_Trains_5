def Length(arr, width) -> int:
    h = 1
    counter = arr[0]
    for i in range(1, len(arr)):
        if counter + 1 + arr[i] > width:
            counter = arr[i]
            h += 1
        else:
            counter += 1 + arr[i]
    return h


def BinSearch(n_mas, m_mas, w) -> int:
    left = 0
    right = w
    n_max = max(n_mas)
    m_max = max(m_mas)
    # print(n_max, m_max)

    if len(n_mas) == 1:
        return max(Length(n_mas, n_mas[0]), Length(m_mas, w - n_mas[0]))
    elif len(m_mas) == 1:
        return max(Length(n_mas, w - m_mas[0]), Length(m_mas, m_mas[0]))

    '''
    if n_max == 1:
        return max(Length(n_mas, 1), Length(m_mas, w - 1))
    elif m_max == 1:
        return max(Length(n_mas, w - 1), Length(m_mas, 1))
    '''
    min_length = max(len(n_mas), len(m_mas))
    while left < right:
        med = (left + right) // 2
        # print(x1, x2, med, left, right)
        if med < n_max:
            left = med + 1
            # print('lol')
        elif w - med < m_max:
            right = med - 1
            # print('kek')
        # elif w - med == med:
            # return max(Length(n_mas, med), Length(m_mas, med))
        else:
            x1 = Length(n_mas, med)
            x2 = Length(m_mas, w - med)
            if x1 >= x2:
                left = med + 1
                min_length = min(max(x1, x2), min_length)
            else:
                right = med
            # print(x1, x2)
            # min_length = min(max(x1, x2), min_length)
    # print(med, right)
    # print(Length(n_mas, left), Length(m_mas, w - left), Length(n_mas, right), Length(m_mas, w - right))
    if right >= n_max and w - right >= m_max:
        min_length = min(max(Length(n_mas, right), Length(m_mas, w - right)), min_length)
    if left >= n_max and w - left >= m_max:
        min_length = min(max(Length(n_mas, left), Length(m_mas, w - left)), min_length)
    return min_length
    # print(Length(n_mas, med), Length(m_mas, w - med), Length(n_mas, right), Length(m_mas, w - right))
    # return max(Length(n_mas, left - 1), Length(n_mas, w - left + 1))


if __name__ == '__main__':
    f = open('input.txt', 'r')
    # w, n, m = map(int, input().split())
    # n_mas = list(map(int, input().split()))
    # m_mas = list(map(int, input().split()))
    w, n, m = map(int, f.readline().split())
    n_mas = list(map(int, f.readline().split()))
    m_mas = list(map(int, f.readline().split()))
    # print(Length(n_mas, 999))
    print(BinSearch(n_mas, m_mas, w))
