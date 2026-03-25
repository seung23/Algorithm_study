from collections import deque

n, m = map(int, input().split())

grid = [[int(x) for x in map(int, input().split())] for _ in range(n)]

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def has_ice():
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                return True
    return False

def bfs():
    q = deque()
    q.append((0, 0))
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    ices = []
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                if grid[nx][ny] == 0:
                    q.append((nx, ny))
                if grid[nx][ny] == 1:
                    ices.append((nx, ny))
    for i, j in ices:
        grid[i][j] = 0
    
    return ices, len(ices)

count = 0
while has_ice():
    count += 1
    ices, leng = bfs()
    
print(count, leng)




