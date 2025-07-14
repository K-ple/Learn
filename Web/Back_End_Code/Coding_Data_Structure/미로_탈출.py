from collections import deque
n,m = map(int,input().split())
queue = deque()
ma = []
for i in range(n):
    ma.append(list(map(int,input())))
mapx = [-1,1,0,0]
mapy = [0,0,-1,1]

def bfs(x,y):
    queue.append([x,y])
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            ax = a + mapx[i]
            bx = b + mapy[i]
            if ax <0 or ax>=n or bx<0 or bx>=m:
                continue
            if ma[ax][bx] == 0:
                continue
            if ma[ax][bx] == 1:
                ma[ax][bx] += ma[a][b]
                queue.append([ax,bx])
    return ma[n-1][m-1] 



answer = bfs(0,0)
print(answer)