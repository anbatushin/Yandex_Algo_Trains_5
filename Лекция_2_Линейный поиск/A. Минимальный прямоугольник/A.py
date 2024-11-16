k = int(input())

x, y = map(int, input().split())
xmin, xmax, ymin, ymax = x, x, y, y
for i in range(k - 1):
    x, y = map(int, input().split())
    if xmin > x:
        xmin = x
    elif xmax < x:
        xmax = x
    if ymin > y:
        ymin = y
    elif ymax < y:
        ymax = y

print(xmin, ymin, xmax, ymax)
