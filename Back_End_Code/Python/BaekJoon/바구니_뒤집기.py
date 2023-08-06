n, m = map(int,input().split())
d = {}
for i in range(1,n+1):
    d[i] = i

for j in range(m):
    count =0
    
    a, b = map(int,input().split())
    li = []
    for k in range(a,b+1):
        li.append(d[k])
    li.reverse()

    for l in range(a,b+1):
        if count != len(li):
            d[l] = li[count]
            count += 1

for m in d.values():
    print(m,end=' ')
    

            