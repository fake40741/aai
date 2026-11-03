#T.C.=O(V+E) S.C=O(V^2)
from collections import deque
grid = [
    ['S', '.', '#'],
    ['#', '.', '#'],
    ['.', '#', 'G']
]
q = deque([[(0, 0)]])
visited = [(0, 0)]
while q:
    path = q.popleft()
    r, c = path[-1]
    if grid[r][c] == 'G':
        print("Path:", path)
        print("Steps:", len(path) - 1)
        break
    for nr, nc in [(r+1,c), (r,c+1), (r-1,c), (r,c-1)]:
        if (0 <= nr < 3 and 0 <= nc < 3 and grid[nr][nc] != '#'
            and (nr,nc) not in visited):
            visited.append((nr,nc))
            q.append(path + [(nr,nc)])
else:
    print("No path exists")
    
