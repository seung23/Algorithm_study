from collections import deque

n, k, u, d = map(int, input().split())

def cango_range(a, b):
    return u <= abs(a-b) <= d

def in_range(a, b):
    return 0 <= a < n and 0 <= b < n

grid = [[int(x) for x in map(int, input().split())] for _ in range(n)]

def comb(arr, start, k, curr, result):
    if len(curr)==k:
        result.append(curr[:])
        return
    for i in range(start, len(arr)):
        curr.append(arr[i])
        comb(arr, i+1, k, curr, result)
        curr.pop()

index_arr = []

for i in range(n):
    for j in range(n):
        index_arr.append((i, j))
result_combs = []
comb(index_arr, 0, k, [], result_combs)

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def bfs(comb):
    q = deque()
    visited = [[False]*n for _ in range(n)]
    count = 0
    for i in range(k):
        x, y = comb[i]
        q.append((x, y))
        visited[x][y] = True
        count += 1
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny] and cango_range(grid[x][y], grid[nx][ny]):
                visited[nx][ny] = True
                q.append((nx, ny))
                count += 1

    return count

max_city = 0
for comb in result_combs:
    max_city = max(max_city, bfs(comb))

print(max_city)
