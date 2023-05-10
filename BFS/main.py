# BFS 예시

from collections import deque

# BFS 메서드
def bfs(gragh, start, visited):
    # 큐를 사용하기 위해 deque 라이브러리 사용
    queue = deque([start])
    
    #현재 노드 방문 처리
    visited[start] = True
    
    # 큐가 전부 비워질때까지 반복
    while queue:
        # 큐에서 원소 하나 뽑아서 출력
        v = queue.popleft()
        print(v, end=' ')
        
        # 아직 방문하지 않은 인접 원소들을 큐에 삽입
        for i in gragh[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드 정보
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8],
          [1, 7]]

# 방문 전이므로 False로 표현
visited = [False] * 9

# BFS 호출
bfs(graph, 1, visited)