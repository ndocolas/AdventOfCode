games = []

win = {3:1, 1:2, 2:3}
los = {2:1, 3:2, 1:3}

for line in open(0).read().splitlines():
    p1, p2 = [ord(x) for x in line.split()]
    p1 -= 64
    p2 -= 87
    if p2 == 1:
        games.append(los.get(p1))
    elif p2 == 2:
        games.append(3+p1)
    else:
        games.append(win.get(p1)+6)

print(sum(games))
