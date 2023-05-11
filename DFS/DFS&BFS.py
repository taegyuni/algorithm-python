# 백준 1260 문제
from collections import deque


def dfs(a, start, visited):
    visited[start] = True
    print(start, end=' ')
    for i in a[start]:
        if not visited[i]:
            dfs(a, i, visited)


def bfs(a, start, visited):
    queue = deque([start])
    visited[start] = False
    while queue:
        c = queue.popleft()
        print(c, end=" ")
        for i in a[c]:
            if visited[i]:
                visited[i] = False
                queue.append(i)


n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()

dfs(graph, v, visited)
print("")
bfs(graph, v, visited)
