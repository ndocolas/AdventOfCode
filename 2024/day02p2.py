count = 0

def safe(lists):
    diffs = [x - y for x, y in zip(lists, lists[1:])]
    return all(1 <= x <= 3 for x in diffs) or all(-1>= x >= -3 for x in diffs)

for report in open(0):
    level = list(map(int, report.split()))

    if any(safe(level[:index] + level[index + 1:]) for index in range(len(level))):
        count+=1

print(count)