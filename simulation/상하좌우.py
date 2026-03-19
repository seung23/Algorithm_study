import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input().strip())

plan = list(input().split())
x, y = 1, 1

for i in range(len(plan)):
    if plan[i] == 'R' and y < N:
        y += 1
    if plan[i] == 'L' and y > 1:
        y -= 1
    if plan[i] == 'U' and x > 1:
        x -= 1
    if plan[i] == 'D' and x < N:
        x += 1

print(x, y)
