from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            queue.append(i)
            visited[i] =True