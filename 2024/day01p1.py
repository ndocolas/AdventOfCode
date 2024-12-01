leftList = []
rightList = []
total = 0
for line in open(0):
    left, right = line.split("   ")

    leftList.append(int(left))
    rightList.append(int(right))

leftList.sort()
rightList.sort()

for x in range(len(rightList)):
    val = abs(rightList.pop())-int(leftList.pop())
    total += val

print(total)