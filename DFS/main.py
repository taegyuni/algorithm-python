# DFS 예시

# DFS 메서드
def dfs(graph, v, visited):
    # 현재 노드 방문처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드 재귀적 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드 정보
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8],
          [1, 7]]

# 방문 전이므로 False로 표현
visited = [False] * 9

# DFS 호출
dfs(graph, 1, visited)