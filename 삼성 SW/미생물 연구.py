import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# (2,2)면 원래 배열 기준: (6,2)
# (5,6)면 원래 배열 기준: (2,5)
# -> 2행부터 6행 전까지 [i in range(2, 6)]
# -> 2열부터 5열 전까지 [j in range(2, 5)]
from collections import deque

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

n, q = map(int, input().split())
arr = [[0]*n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def mark(num, r1, c1, r2, c2):
    for i in range(r1, r2):  # (2, 6)
        arr[i][c1:c2] = [num]*(c2-c1) # (2, 5)

def find_cells(num):
    cells = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == num:
                cells.append((i, j))

    return cells

def del_seperated(num):
    cells = find_cells(num)
    if not cells:
        return

    visited = set()
    q = deque()
    q.append(cells[0])
    visited.add(cells[0])

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and (nx, ny) not in visited and arr[nx][ny] == num:
                visited.add((nx, ny))
                q.append((nx, ny))

    if len(visited) < len(cells):
        for (i, j) in cells:
            arr[i][j] = 0

def try_place(num, n_arr, cell_info):
    min_r = min(r for r, c in cell_info)
    min_c = min(c for r, c in cell_info)
    shape = [(r-min_r, c-min_c) for r, c in cell_info]

    for dc in range(n):
        for dr in range(n-1, -1, -1):
            ok = True
            for sr, sc in shape:
                nr, nc = sr + dr, sc + dc
                if not in_range(nr, nc) or n_arr[nr][nc] != 0:
                    ok = False
                    break
            if ok:
                for sr, sc in shape:
                    n_arr[sr+dr][sc+dc] = num
                return True
    return False

def calc_score(n_arr):
    pairs = set()
    area = {}

    for i in range(n):
        for j in range(n):
            if n_arr[i][j] != 0:
                num = n_arr[i][j]
                area[num] = area.get(num, 0) + 1

    for i in range(n):
        for j in range(n):
            if n_arr[i][j] != 0:
                for dx, dy in zip(dxs, dys):
                    nx, ny = i + dx, j + dy
                    if in_range(nx, ny) and n_arr[nx][ny] != 0 and n_arr[nx][ny] != n_arr[i][j]:
                        a, b = min(n_arr[nx][ny], n_arr[i][j]), max(n_arr[nx][ny], n_arr[i][j])
                        pairs.add((a,b))

    score = 0
    for a, b in pairs:
        score += area[a] * area[b]
    return score

cells_info = []
for num in range(1, q+1):
    a, b, c, d = map(int, input().split())
    r1, c1, r2, c2 = n-d, a, n-b, c # 2, 2, 6, 5
    mark(num, r1, c1, r2, c2)
    for i in range(1, num):
        del_seperated(i)
    cells_info = []
    for i in range(1, num + 1):
        cells = find_cells(i)
        if cells:
            cells_info.append([i, len(cells), cells]) # num, 길이, 좌표 정보
    cells_info.sort(key=lambda x: (-x[1], x[0])) # 길이기준 정렬
    n_arr = [[0]*n for _ in range(n)]
    for num_id, length, cell_info in cells_info:
        try_place(num_id,n_arr,cell_info)

    print(calc_score(n_arr))

    arr = n_arr



