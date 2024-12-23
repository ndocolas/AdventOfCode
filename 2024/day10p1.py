from collections import deque

grid = [list(map(int, line.strip())) for line in open(0).readlines()]

rows = len(grid)
cols = len(grid[0])

zeros = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 0]

def scores(grid, r, c):
    q = deque([(r, c)])
    summits = 0
    seen = {(r, c)}
    while len(q) > 0:
        cr, cc = q.popleft()
        for nr, nc in [(cr - 1, cc), (cr, cc + 1), (cr + 1, cc), (cr, cc - 1)]:
            if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
            if grid[nr][nc] != grid[cr][cc] + 1: continue
            if (nr, nc) in seen: continue
            seen.add((nr, nc))
            if grid[nr][nc] == 9:
                summits += 1
            else:
                q.append((nr, nc))
    return summits

print(sum(scores(grid, r, c) for r, c in zeros))