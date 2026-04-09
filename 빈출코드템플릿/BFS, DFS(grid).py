from collections import deque

grid = [
    [1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 1, 1, 0],
    [1, 1, 1, 0, 0],
]
N = len(grid)      # 행 개수
M = len(grid[0])   # 열 개수

# 상하좌우 방향 (이게 그리드의 '인접 리스트' 역할)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(sy, sx):
    visited = [[False] * M for _ in range(N)]
    q = deque([(sy, sx)])
    visited[sy][sx] = True
    
    while q:
        y, x = q.popleft()
        print((y, x), end=' ')
        
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            
            # ① 격자 범위 체크
            if not (0 <= ny < N and 0 <= nx < M):
                continue
            # ② 방문 체크
            if visited[ny][nx]:
                continue
            # ③ 문제 조건 체크 (예: 1인 칸만 이동 가능)
            if grid[ny][nx] == 0:
                continue
            
            visited[ny][nx] = True
            q.append((ny, nx))



import sys
sys.setrecursionlimit(10**6)   # 그리드 크면 필수!

visited = [[False] * M for _ in range(N)]

def dfs(y, x):
    visited[y][x] = True
    print((y, x), end=' ')
    
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        
        if not (0 <= ny < N and 0 <= nx < M):
            continue
        if visited[ny][nx]:
            continue
        if grid[ny][nx] == 0:
            continue
        
        dfs(ny, nx)