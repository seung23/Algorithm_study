import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, k, l = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
robot_list = [tuple(int(x-1) for x in map(int, input().split())) for _ in range(k)]
robot_set = set(robot_list)

def is_robot(x, y):
    return (x, y) in robot_set # set기반 변경해서 O(1)로 만들기


def can_go(x, y):
    return 0 <= x < n and 0 <= y < n and grid[x][y] != -1

from collections import deque

init_dxs = [-1, 0, 0, 1]
init_dys = [0, -1, 1, 0] # 상좌우하 (행, 열 우선순위 고려)

def init_bfs(robot):
    q = deque()
    a, b = robot
    if grid[a][b] > 0:         # 시작점에 먼지 있으면 이동 불필요
        return (a, b)
    visited = [[False]*n for _ in range(n)]
    q.append((a, b))
    visited[a][b] = True
    while q:
        x, y = q.popleft()
        for init_dx, init_dy in zip(init_dxs, init_dys):
            nx, ny = x + init_dx, y + init_dy
            if can_go(nx, ny) and not visited[nx][ny] and not is_robot(nx, ny):
                visited[nx][ny] = True
                if grid[nx][ny] > 0:
                    return (nx, ny)   
                else:
                    q.append((nx, ny))
    return (a, b)              # None 대신 현재 위치 반환

              
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0] # 우하좌상 (해당 방향에서 +2 방향은 건너뛰고 가야할듯 / 본인 자리 포함하기)

def clean():
    q = deque()
    for robot in robot_list:
        x, y = robot
        result = []
        val_grid = [[(x, y)] for _ in range(4)]          
        for i in range(4):
            dust = grid[x][y]                              
            for j in range(4):
                if j != (i+2)%4 :
                    nx, ny = x + dxs[j], y + dys[j]
                    if can_go(nx, ny):                            
                        dust += grid[nx][ny]
                        val_grid[i].append((nx, ny))                            
            result.append((i, dust))
        result.sort(key=lambda x: (-x[1], x[0]))
        grid_dir, _ = result[0]
        for vgrid in val_grid[grid_dir]:
            x, y = vgrid
            if grid[x][y] <= 20:
                grid[x][y] = 0
            else:
                grid[x][y] -= 20

def dust_ac():
    global grid
    idx_list = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                grid[i][j] += 5
            elif grid[i][j] == 0:
                idx_list.append((i, j))

    return idx_list

def dust_dif(idx_list):
    global grid
    dif_list = []
    for idx in idx_list:
        x, y = idx
        dustsum = 0
        flag = True
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny) and grid[nx][ny] > 0:
                dustsum += grid[nx][ny]
                if flag:
                    dif_list.append((x, y))
                    flag = False
        if dustsum != 0:
            dif_list.append(dustsum//10)
    for i in range(0, len(dif_list), 2):
        grid[dif_list[i][0]][dif_list[i][1]] = dif_list[i+1]

for _ in range(l):       
    for i in range(k):
        old_pos = robot_list[i]
        new_pos = init_bfs(robot_list[i])
        if old_pos != new_pos:
            robot_set.discard(old_pos)
            robot_set.add(new_pos)
        robot_list[i] = new_pos
    clean()
    idx_list = dust_ac()
    dust_dif(idx_list)
    ans = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                ans += grid[i][j]
    print(ans)
