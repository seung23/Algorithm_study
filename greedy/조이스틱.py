def solution(name):
    n = len(name)
    
    # 1. 상하 조작 횟수
    up_down = sum(min(ord(c) - ord('A'), ord('Z') - ord(c) + 1) for c in name)
    
    # 2. 좌우 조작 횟수 최솟값
    move = n - 1
    
    for i in range(n):
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':
            next_i += 1
        move = min(move, i * 2 + (n - next_i), i + (n - next_i) * 2)
    
    return up_down + move