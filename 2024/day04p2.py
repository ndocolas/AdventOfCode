matrix = [list(line.strip()) for line in open(0).readlines()]

total = 0

rows = len(matrix)
cols = len(matrix[0])

# Directions: Down-Right, Down-Left, Up-Left, Up-Right
dRow = [1, 1, -1,-1]
dCol = [1,-1, -1, 1]

def check_sonar(i, j):
    global total
    if(matrix[i][j] == "A"):
        word = ""
        for dir in range(4):
            row = i + dRow[dir]
            col = j + dCol[dir]
            if (0 <= row < rows and 0 <= col < cols):
                word += matrix[row][col]
                row = i + dRow[dir]
                col = j + dCol[dir]
            else:
                break
        if(word.count("M") == 2 and word.count("S") == 2):
            if not (word[0] == word[2] and word[1] == word[3]):
                total +=1

for i in range(rows):
    for j in range(cols):
        check_sonar(i, j)

print(total)
