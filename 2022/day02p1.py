games = []

for line in open(0):
    p1, p2 = [ord(val) for val in line.split()]
    p1 -= 64
    p2 -= 87

    if(p2==p1):
        games.append(3)
    elif((p2 == 1 and p1 == 3) or (p2 == 2 and p1 == 1) or (p2 == 3 and p1 == 2)):
        games.append(6)

    games.append(p2)

print(sum(games))