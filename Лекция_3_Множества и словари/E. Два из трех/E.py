def ListOfNums(sets) -> list:
    res_set = set()
    for index in range(3):
        res_set |= sets[index] & sets[(index + 1) % 3]
    return list(sorted(res_set))


if __name__ == '__main__':
    lst_of_sets = [] * 3
    for i in range(3):
        input()
        lst_of_sets.append(set())
        for elem in map(int, input().split()):
            lst_of_sets[i].add(elem)
    print(' '.join(map(str, ListOfNums(lst_of_sets))))
