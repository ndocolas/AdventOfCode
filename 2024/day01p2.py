leftList = []
rightList = []
total = 0
for line in open(0):
    left, right = line.split("   ")

    leftList.append(int(left))
    rightList.append(int(right))

for x in range(len(rightList)):
    total += leftList[x]*rightList.count(leftList[x])

print(total)