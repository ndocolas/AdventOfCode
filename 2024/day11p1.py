stones = input().split()

list = []

for _ in range(25):
    for stone in stones:
        if stone == "0":
            list.append("1")
            continue
        if len(stone) % 2 == 0:
            list.append(stone[:len(stone)//2].lstrip("0") or "0")
            list.append(stone[len(stone)//2:].lstrip("0") or "0")
            continue
        list.append(str(int(stone)*2024))
        continue
    else:
        stones = list
        list = []

print(len(stones))

        