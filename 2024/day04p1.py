matrix = [list(line.strip()) for line in open(0).readlines()]

total = 0

rows = len(matrix)
cols = len(matrix[0])

# Directions: Right, Down-Right, Down, Down-Left, Left, Up-Left, Up, Up-Right
dRow = [0, 1, 1, 1, 0, -1, -1, -1]
dCol = [1, 1, 0, -1, -1, -1, 0, 1]

def check_sonar(i, j):
    global total
    for dir in range(8):
        word = matrix[i][j]
        row = i + dRow[dir]
        col = j + dCol[dir]
        for _ in range(3):
            if 0 <= row < rows and 0 <= col < cols:
                word += matrix[row][col]
                row += dRow[dir]
                col += dCol[dir]
            else:
                break
        if(word=="XMAS"):
            total += 1

for i in range(rows):
    for j in range(cols):
        check_sonar(i, j)

print(total)
