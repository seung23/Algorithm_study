import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

from collections import deque

n, t = map(int, input().split())
f_arr = [list(input().strip()) for _ in range(n)]
b_arr = [list(map(int, input().split())) for _ in range(n)]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1] # 상하좌우

# T=1, C=2, M=4 비트마스크로 표현하자. (OR 연산 수월)
for i in range(n):
    for j in range(n):
        if f_arr[i][j] == "T":
            f_arr[i][j] = 1
        elif f_arr[i][j] == "C":
            f_arr[i][j] = 2
        elif f_arr[i][j] == "M":
            f_arr[i][j] = 4

def add_1():
    for i in range(n):
        for j in range(n):
            b_arr[i][j] += 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n



# bfs로 한 점 찍고 f_arr 값 같은쪽으로만 진행
# -> b_arr 값 -1씩 하기, count +1씩 하기, 최댓값 좌표 업데이트
# 더 이상 진행 못하면(q 다쓰면) b_arr[최댓값좌표] += count

def make_group():
    visited = [[False]*n for _ in range(n)]
    rep_list = []
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                count = 1
                max_i, max_j = i, j
                b_arr[i][j] -= 1
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                while q:
                    x, y = q.popleft()
                    for dx, dy in zip(dxs, dys):
                        nx, ny = x + dx, y + dy
                        if in_range(nx, ny) and not visited[nx][ny] and f_arr[x][y] == f_arr[nx][ny]:
                            visited[nx][ny] = True
                            b_arr[nx][ny] -= 1
                            count += 1
                            if b_arr[nx][ny] > b_arr[max_i][max_j]:
                                max_i, max_j = nx, ny
                            elif b_arr[nx][ny] == b_arr[max_i][max_j]:
                                if (nx, ny) < (max_i, max_j):  # 튜플 비교: 행 먼저, 같으면 열
                                    max_i, max_j = nx, ny
                            q.append((nx, ny))
                rep_list.append((max_i, max_j))
                b_arr[max_i][max_j] += count

    return rep_list

def bit_count(r, c):
    return bin(f_arr[r][c]).count('1')

def det_order(rep_list):
    rep_list.sort(key=lambda x: (x[0], x[1]))
    group1 = []
    group2 = []
    group3 = []
    for r, c in rep_list:
        if bit_count(r, c) == 1:
            group1.append((r, c))
        elif bit_count(r, c) == 2:
            group2.append((r, c))
        elif bit_count(r, c) == 3:
            group3.append((r, c))

    group1.sort(key=lambda x: -b_arr[x[0]][x[1]])
    group2.sort(key=lambda x: -b_arr[x[0]][x[1]])
    group3.sort(key=lambda x: -b_arr[x[0]][x[1]])

    return group1 + group2 + group3

def propa(sorted_rep):
    defended = set()    #  **** set으로 관리 ****
    for r, c in sorted_rep:
        if (r, c) in defended:    # **** set에서 찾는거라 O(1) ****
            continue
        move_dir = b_arr[r][c]%4
        x = b_arr[r][c]-1
        b_arr[r][c] = 1
        prop_food = f_arr[r][c]
        while x > 0:
            nr, nc = r + dxs[move_dir], c + dys[move_dir]
            if in_range(nr, nc):
                if prop_food == f_arr[nr][nc]:
                    r, c = nr, nc
                    continue

                elif x > b_arr[nr][nc]: # 강한 전파
                    x -= b_arr[nr][nc] + 1
                    b_arr[nr][nc] += 1
                    f_arr[nr][nc] = prop_food
                    r, c = nr, nc
                    if (nr, nc) in sorted_rep:
                        defended.add((nr, nc))

                elif x <= b_arr[nr][nc]: # 약한 전파
                    b_arr[nr][nc] += x
                    x = 0
                    f_arr[nr][nc] = f_arr[nr][nc] | prop_food # or로 합치기
                    r, c = nr, nc
                    if (nr, nc) in sorted_rep:
                        defended.add((nr, nc))

            else:
                break


# 민트: 1, 초코: 2, 우유: 4
# 민트초코: 3, 민트우유: 5, 초코우유: 6
# 민트초코우유: 7
for _ in range(t):
    add_1()
    rep_list = make_group()
    sorted_rep = det_order(rep_list)
    propa(sorted_rep)
    ans = [0]*7
    for i in range(n):
        for j in range(n):
            if f_arr[i][j] == 7:
                ans[0] += b_arr[i][j]
            elif f_arr[i][j] == 3:
                ans[1] += b_arr[i][j]
            elif f_arr[i][j] == 5:
                ans[2] += b_arr[i][j]
            elif f_arr[i][j] == 6:
                ans[3] += b_arr[i][j]
            elif f_arr[i][j] == 4:
                ans[4] += b_arr[i][j]
            elif f_arr[i][j] == 2:
                ans[5] += b_arr[i][j]
            elif f_arr[i][j] == 1:
                ans[6] += b_arr[i][j]

    print(*ans)



