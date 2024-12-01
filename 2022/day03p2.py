map_char = {x: i+1 for i, x in enumerate(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))}
isolates = []
final_char = []
lines = open(0).readlines()

for i in range(0, len(lines), 3):
    isolates.append([line.strip() for line in lines[i:i+3]])

for l in isolates:
    single = set(l[0]) & set(l[1]) & set(l[2])
    if single:
        for x in single:
            final_char.append(map_char.get(x))

print(sum(final_char))