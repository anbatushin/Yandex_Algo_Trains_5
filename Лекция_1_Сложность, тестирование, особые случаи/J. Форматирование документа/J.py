def SortList():
    for i in range(len(lst) // 4):
        for j in range(len(lst) // 4 - i - 1):
            if lst[j * 4] > lst[j * 4 + 4]:
                for k in range(4):
                    lst[j * 4 + k], lst[j * 4 + 4 + k] = lst[j * 4 + 4 + k], lst[j * 4 + k]


def Check(length):
    global posx, image_surr, first

    for i in range(len(lst) // 4):
        if first and (posx >= lst[i * 4 + 1] or posx + length <= lst[i * 4] or posy >= lst[i * 4 + 3]):
            continue
        elif not first and (posx >= lst[i * 4 + 1] or posx + length + c <= lst[i * 4] or posy >= lst[i * 4 + 3]):
            continue
        else:
            image_surr = True
            posx = lst[i * 4 + 1]
            first = True

    return (posx + length <= w) if first else (posx + length + c <= w)


def NextStr():
    global posx, posy, hmax, first, image_surr, last
    posx, posy = 0, posy + hmax
    hmax, first, image_surr = h, True, False
    last[0], last[1] = posx, posy


def NewWord(length):
    global posx, first

    while True:
        if Check(length):
            if image_flag and not first:
                print(posx + c, posy)
                posx += length + c
            elif image_flag and first:
                print(posx, posy)
                posx += length
                first = False
            else:
                posx += length + (c if not first else 0)
                first = False
            return
        else:
            NextStr()


def NewImage():
    global posx, posy, hmax, first, last

    layout, dx, dy, width, height = '', 0, 0, 0, 0
    for word in image:
        if word.startswith("layout"):
            layout = word[7:-1] if word == image[-1] else word[7:]
        elif word.startswith("width"):
            width = int(word[6:-1] if word == image[-1] else word[6:])
        elif word.startswith("height"):
            height = int(word[7:-1] if word == image[-1] else word[7:])
        elif word.startswith("dx"):
            dx = int(word[3:-1] if word == image[-1] else word[3:])
        elif word.startswith("dy"):
            dy = int(word[3:-1] if word == image[-1] else word[3:])

    if layout == 'floating':
        nx, ny = last[0] + dx, last[1] + dy
        nx = max(0, min(nx, w - width))
        print(nx, ny)
        last = [nx + width, ny]
    elif layout == 'surrounded':
        first = True
        NewWord(width)
        last = [posx, posy]
        first = True
        lst.extend([posx - width, posx, posy, posy + height])
        if len(lst) > 4:
            SortList()
    elif layout == 'embedded':
        NewWord(width)
        last = [posx, posy]
        hmax = max(hmax, height)


f = open("input.txt", "r")
lines = f.readlines()

w, h, c = map(int, lines[0].split())
lst, image = [], []
posx, posy, hmax = 0, 0, h
first, image_flag, image_surr = True, False, False
last = [0, 0]

for line in lines[1:]:
    if line in ('\n', '', ' '):
        NextStr()
    else:
        for word in line.split():
            if word[0] != '(' and not image_flag:
                NewWord(len(word) * c)
                last = [posx, posy]
            elif word[0] == '(':
                image_flag, image = True, [word]
            else:
                image.append(word)
                if word[-1] == ')':
                    NewImage()
                    image_flag = False
                    image.clear()
