n, m = map(int,input().split())
d = {}
for i in range(1,n+1):
    d[i] = i
for j in range(m):
    a, b = map(int, input().split())
    check = d[a]
    d[a] = d[b]
    d[b] = check

for k in d.values():
    print(k,end=" ")