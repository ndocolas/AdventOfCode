file = open(0)

rules = []

for line in file:
    if line.isspace(): break
    rules.append(list(map(int, line.strip().split("|"))))

cache = {}

for x,y in rules:
    cache[(x,y)] = True
    cache[(y,x)] = False

def is_ordered(page):
    for i in range(len(page)):
        for j in range(i + 1, len(page)):
            key = (page[i], page[j])
            if key in cache and not cache[key]:
                return False
    return True

total = 0

for line in file:
    page = list(map(int, line.strip().split(",")))
    if is_ordered(page):
        total += page[len(page) // 2]

print(total)