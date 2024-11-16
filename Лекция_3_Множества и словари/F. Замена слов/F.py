_end = '_end_'


def make_trie(dct) -> dict:
    root = {}
    for prefix in dct:
        curr_dct = root
        for ch in prefix:
            curr_dct = curr_dct.setdefault(ch, {})
        curr_dct[_end] = _end
    return root


def in_trie(trie, word) -> (bool, str):
    current_dct = trie
    pref = []
    for ch in word:
        pref.append(ch)
        if ch not in current_dct:
            return False, ''.join(pref)
        if _end in current_dct[ch]:
            return True, ''.join(pref)
        current_dct = current_dct[ch]
    return False, ''.join(pref)


def NewStr(dct, s) -> list:
    res = []
    pref_dct = make_trie(dct)
    # print(pref_dct)
    for word in s:
        answer = in_trie(pref_dct, word)
        # print(word)
        # print(answer)
        fl = answer[0]
        new_word = answer[1]
        if fl:
            res.append(new_word)
        else:
            res.append(word)
    # print(pref_dct)
    return res


if __name__ == '__main__':
    dictionary = input().split()
    str = input().split()
    print(' '.join(NewStr(dictionary, str)))
