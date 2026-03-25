import copy

def solve():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    dxs = [-1, 0, 1, 0, 0]
    dys = [0, 1, 0, -1, 0]
    
    def in_range(x, y):
        return 0 <= x < n and 0 <= y < m
    
    def click(grid, x, y):
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny):
                grid[nx][ny] ^= 1  # toggle
    
    ans = float('inf')
    
    # 첫 행 클릭 패턴 완전탐색 (2^m 가지)
    for bit in range(1 << m):
        grid = copy.deepcopy(board)
        cnt = 0
        
        # 1행 클릭 적용
        for j in range(m):
            if bit & (1 << j):
                click(grid, 0, j)
                cnt += 1
        
        # 2행~n행은 윗행 기준으로 강제 결정
        for i in range(1, n):
            for j in range(m):
                if grid[i-1][j] == 0:  # 윗칸이 0이면 반드시 클릭
                    click(grid, i, j)
                    cnt += 1
        
        # 마지막 행 전부 1인지 확인
        if all(grid[n-1][j] == 1 for j in range(m)):
            ans = min(ans, cnt)
    
    print(ans if ans != float('inf') else -1)

solve()
