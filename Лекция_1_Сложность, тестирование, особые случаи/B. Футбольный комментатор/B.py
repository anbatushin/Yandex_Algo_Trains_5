g1 = list(input())
g2 = list(input())
num = int(input())

g1_left = int(g1[0])
g1_right = int(g1[2])
g2_left = int(g2[0])
g2_right = int(g2[2])

sum = g1_right - g1_left + g2_right - g2_left

if sum < 0:
    print(0)
elif num == 1:
    if g1_right >= g2_left + sum:
        print(sum + 1)
    else:
        print(sum)
elif num == 2:
    if g2_right >= g1_left:
        print(sum + 1)
    else:
        print(sum)
