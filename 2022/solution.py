list = {x: i+1 for i, x in enumerate(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))}
isolates = []
lines = open(0).readlines()

for i in range(0, len(lines), 3):
    isolates.append([line.strip() for line in lines[i:i+3]])


    


    # sets = set(p1) & set(p2)
    # if sets:
    #     for x in sets:
    #         isolates.append(list.get(x))

print(isolates)