import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
input = input().strip()

x = int(input[1])
y = int(ord(input[0])) - int(ord("a")) + 1

dx = [-2, -2, 2, 2, -1, -1, 1, 1]
dy = [-1, 1, -1, 1, 2, -2, 2, -2]

count = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx > 8 or nx < 1 or ny > 8 or ny < 1:
        continue

    count += 1

print(count)