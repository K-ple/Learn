n, m = map(int,input().split())
d = {}
for i in range(1,n+1):
    d[i] = 0
for j in range(m):
    a,b,c = map(int,input().split())
    for k in range(a,b+1):
        d[k] = c

for l in d.values():
    print(l, end=' ')