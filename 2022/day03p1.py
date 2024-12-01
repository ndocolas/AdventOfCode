map_char = {x: i+1 for i, x in enumerate(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))}
isolates = []

for line in open(0):
    mid = len(line)//2
    left = line[:mid]
    right = line[mid:]
    intersection = set(left) & set(right)
    if intersection:
        for x in intersection:
            isolates.append(map_char.get(x))

print(sum(isolates))