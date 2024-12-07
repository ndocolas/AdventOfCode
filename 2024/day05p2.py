import functools

file = open(0)

rules = []

for line in file:
    if line.isspace(): break
    rules.append(list(map(int, line.strip().split("|"))))

cache = {}

for x, y in rules:
    cache[(x ,y)] = -1
    cache[(y ,x)] = 1

def is_ordered(page):
    for i in range(len(page)):
        for j in range(i + 1, len(page)):
            key = (page[i], page[j])
            if key in cache and cache[key] == 1:
                return False
    return True

def cmp(x, y):
    return cache.get((x,y), 0)

total = 0

for line in file:
    page = list(map(int, line.strip().split(",")))
    if is_ordered(page): continue
    page.sort(key=functools.cmp_to_key(cmp))
    total += page[len(page) // 2]

print(total)