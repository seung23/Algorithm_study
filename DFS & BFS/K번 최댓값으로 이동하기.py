import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())
grid = [[int(x) for x in input().split()] for _ in range(n)]
start = list(map(int, input().split()))
sx, sy = start[0]-1, start[1]-1

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(sx, sy):
    visited = [[False]*n for _ in range(n)]  
    visited[sx][sy] = True
    q = deque([(sx, sy)])
    candidates = []  

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] < grid[sx][sy]:
                visited[nx][ny] = True
                candidates.append((grid[nx][ny], nx, ny))
                q.append((nx, ny))

    return candidates

for _ in range(k):
    candidates = bfs(sx, sy)
    if not candidates:
        break
    
    # 최댓값 기준, 행 작은 것, 열 작은 것 순으로 정렬
    candidates.sort(key=lambda c: (-c[0], c[1], c[2]))
    _, sx, sy = candidates[0]

print(sx+1, sy+1)