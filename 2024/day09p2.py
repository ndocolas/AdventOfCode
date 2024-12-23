from itertools import groupby

amphipod = [int(x) for x in open(0).read().strip()]

archive = True
sequence = []
num = 0
for val in amphipod:
    if archive:
        archive = False
        sequence.extend([num] * val)
        num+=1
    else:
        archive = True
        sequence.extend([-1] * val)

blanks = [
    [i for i, x in group]
    for key, group in groupby(enumerate(sequence), lambda ix: ix[1] == -1)
    if key
]

def swap(blank, file, end):
    for val in file:
        blank_index = blank.pop(0)
        if blank_index > end: return blank, False
        sequence[blank_index] = val
    return blank, True
        

pStart = 0
pEnd = len(sequence) - 1
while pStart < pEnd:
    group = []
    while sequence[pEnd] == -1:
        pEnd -= 1
    val = sequence[pEnd]
    size = 0
    while sequence[pEnd] == val:
        size += 1
        group.append(sequence[pEnd])
        pEnd -= 1
    for blank in blanks:
        if(len(blank) >= len(group)):
            blank, cont = swap(blank, reversed(group), pEnd)
            if(cont):
                pend_sup = pEnd+1
                for i in range(size):
                    sequence[pend_sup+i] = -1
                break

total = 0

for i, num in enumerate(sequence):
    if num == -1: continue
    total += (num*i)

print(total)
    
