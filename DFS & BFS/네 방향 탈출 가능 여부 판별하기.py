n, m = map(int, input().split())
grid = [[x for x in map(int, input().split())] for _ in range(n)]
visited = [[False] * m for _ in range(n)]

from collections import deque

def bfs():
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    while q:
        curr_v = q.popleft()
        x, y = curr_v
        if x == n-1 and y == m-1:
            return True

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                q.append((new_x, new_y))
    
    return False
         

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid [x][y] == 0:
        return False
    return True 


x, y = 0, 0
q = deque([(x, y)])
print(q)
visited[0][0] = True

if bfs():
    print(1)
else:
    print(0)
