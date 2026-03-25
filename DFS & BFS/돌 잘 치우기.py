from collections import deque

n, k, m = map(int, input().split())
grid = [[int(x) for x in input().split()] for _ in range(n)]
start_list = [tuple(int(x)-1 for x in input().split()) for _ in range(k)]

stones = []
for i, row in enumerate(grid):
    for j, v in enumerate(row):
        if v == 1:
            stones.append((i, j))

def comb(stones, start, m, current, result):
    if len(current) == m:
        result.append(current[:])
        return
    for i in range(start, len(stones)):
        current.append(stones[i])
        comb(stones, i+1, m, current, result)
        current.pop()

stones_cand = []
comb(stones, 0, m, [], stones_cand)

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(grid):
    visited = [[False]*n for _ in range(n)]
    q = deque()
    for x, y in start_list:
        visited[x][y] = True
        q.append((x, y))
    
    count = 0  
    while q:
        x, y = q.popleft()
        count += 1  
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny))
    return count

grid_o = [row[:] for row in grid]

max_count = 0
for cand in stones_cand:
    grid = [row[:] for row in grid_o] 
    for a, b in cand:
        grid[a][b] = 0
    max_count = max(max_count, bfs(grid))

print(max_count)