from collections import deque

grid = [list(line.strip()) for line in open(0)]

rows = len(grid)
cols = len(grid[0])

regions = []
seen = set()

for r in range(rows):
    for c in range(cols):
        if (r, c) in seen: continue
        seen.add((r, c))
        q = deque([(r, c)])
        region = {(r, c)}
        crop = grid[r][c]
        while q:
            cr, cc = q.popleft()
            for nr, nc in [(cr+1, cc), (cr-1, cc), (cr, cc+1), (cr, cc-1)]:
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
                if (nr, nc) in region: continue
                if grid[nr][nc] != crop: continue
                region.add((nr, nc))
                q.append((nr, nc))
        seen |= region
        regions.append(region)

def sides(region):
    corner_candidates = set()
    for r, c in region:
        for cr, cc in [(r - 0.5, c - 0.5), (r + 0.5, c - 0.5), (r + 0.5, c + 0.5), (r - 0.5, c + 0.5)]:
            corner_candidates.add((cr, cc))
    sides = 0
    for r, c in corner_candidates:
        config = [(cr, cc) in region for cr, cc in [(r - 0.5, c - 0.5), (r + 0.5, c - 0.5), (r + 0.5, c + 0.5), (r - 0.5, c + 0.5)]]
        corners = sum(config)
        if corners == 1:
            sides += 1
        elif corners == 2:
            if config == [False, True, False, True] or config == [True, False, True, False]:
                sides += 2
        elif corners == 3:
            sides += 1
    return sides


print(sum(len(region) * sides(region) for region in regions))
        
        
    
        
                