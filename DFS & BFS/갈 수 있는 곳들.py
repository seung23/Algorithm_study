n, k = map(int, input().split())

grid = [[int(x) for x in map(int, input().split())] for _ in range(n)]
start = [[int(x-1) for x in map(int, input().split())] for _ in range(k)]

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

visited = [[False for _ in range(n)] for _ in range(n)]

from collections import deque

q = deque(start)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 1:
        return False
    return True

count = 0 

def bfs():
    global count
    while q:
        x, y = q.popleft()
        if not visited[x][y]:
            visited[x][y] = True
            count += 1
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                count += 1
                q.append([new_x, new_y])

bfs()
print(count)


