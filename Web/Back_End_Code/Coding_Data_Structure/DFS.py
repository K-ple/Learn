def dfs(graph, v, visited):
    visited[v] =True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
v = int(input())
graph = []
visited = [False] * len(v)

