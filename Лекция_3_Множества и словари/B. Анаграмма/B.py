from collections import Counter


s1 = input()
s2 = input()
if Counter(s1) == Counter(s2):
    print('YES')
else:
    print('NO')
