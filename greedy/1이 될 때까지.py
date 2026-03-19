import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
count = 0

while N >= K:
    while N % K != 0:
        N -= 1
        count += 1
    N //= K
    count += 1

count += (N - 1)
print(count)
