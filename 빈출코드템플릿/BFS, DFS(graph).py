from collections import deque

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [], 5: [], 6: []
}

# ---------- BFS ----------
def bfs(start):
    visited = [False] * 7
    q = deque([start])
    visited[start] = True
    while q:
        node = q.popleft()      # ← 앞에서 꺼냄 (FIFO)
        print(node, end=' ')
        for nx in graph[node]:
            if not visited[nx]:
                visited[nx] = True
                q.append(nx)


# ---------- DFS (재귀 버전) ----------
visited = [False] * 7
def dfs(node):
    visited[node] = True
    print(node, end=' ')
    for nx in graph[node]:
        if not visited[nx]:
            dfs(nx)

bfs(1)
print("__")
dfs(1)