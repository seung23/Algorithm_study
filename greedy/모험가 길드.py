import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input().strip())

group = list(map(int, input().split()))

group.sort()
count = 0
result = 0 

for i in group:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)

# for i in group 이 포인트!
# for i in range()를 관성적으로 쓰지 말자.
 


    
    