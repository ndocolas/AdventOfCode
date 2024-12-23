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

pStart = 0
pEnd = len(sequence) - 1
while pStart < pEnd:
    if(sequence[pStart] == -1):
        while sequence[pEnd] == -1:
            pEnd -= 1
        sequence[pStart], sequence[pEnd] = sequence[pEnd], sequence[pStart]
    pStart+=1

print(sum(i * x for i, x in enumerate(sequence[:pStart])))
    
