import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, t = map(int, input().split())
move_list = input().strip()
grid = [list(map(int, input().split())) for _ in range(n)]

sx, sy = n//2, n//2
result = grid[sx][sy]
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1] #상우하좌

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

move_dir = 0
for move in move_list:
    if move == "F":
        nx, ny = sx + dxs[move_dir], sy + dys[move_dir]
        if in_range(nx, ny):
            sx, sy = nx, ny
            result += grid[sx][sy]
    elif move == "R":
        move_dir = (move_dir+1) % 4
    elif move == "L":
        move_dir = (move_dir-1) % 4

print(result)