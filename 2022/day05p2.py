list = [[(y[0].split("-")), y[1].split("-")] for y in [x.strip().split(",") for x in open(0)]]
t = 0
for intervals in list:
    firList = intervals[0]
    secList = intervals[1]

    firIn = []
    secIn = []

    for val in range(int(firList[0]), int(firList[1])+1):
        firIn.append(val)

    for val in range(int(secList[0]), int(secList[1])+1):
        secIn.append(val)

    if set(firIn) & set(secIn):
        t+=1

print(t)