matrix = list(map(list, open(0).read().splitlines()))

rows = len(matrix)
cols = len(matrix[0])

row, col = 0, 0

for i in range(rows):
    for j in range(cols):
        if(matrix[i][j] == "^"): row, col = i, j
        
dRow = -1
dCol = 0

dir = 0
positions = set()

while True:
    positions.add((row, col))
    if 0 > row+dRow or row+dRow >= rows or 0 > col+dCol or  col+dCol >= cols: break
    if(matrix[row+dRow][col+dCol] == "#"):
        dCol, dRow = -dRow, dCol
    else:
        row += dRow
        col += dCol

print(len(positions))