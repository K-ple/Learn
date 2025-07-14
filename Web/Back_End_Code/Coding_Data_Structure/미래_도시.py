n, m = map(int,input().split())
inf = int(1e9)
w = [inf]*(n+1)
graph = [[] for i in range(n+1)]
w[1] = 0

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append([b,1])


def warp():
    for i in range(1,n+1):
        for j in graph[i]:
            if w[j[0]] > j[1]+w[i]:
                w[j[0]] = j[1]+w[i]

warp()
x, k = map(int,input().split())
answer = w[k]

w = [inf]*(n+1)
if x < k:
    w[x] = 0
    warp()
    answer += w[k]
elif k < x:
    w[k] = 0
    warp()
    answer += w[x]

if answer >= inf:
    print(-1)
else:
    print(answer)