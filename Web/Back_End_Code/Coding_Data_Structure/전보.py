n ,m,c = map(int,input().split())

inf = int(1e9)
city = [[] for i in range(n+1)]
visited = [False] *(n+1)
time = [0]*(n+1)

time[c] = 0

for _ in range(m):
    x,y,z = map(int,input().split())
    city[x].append((y,z))

def smallest_node():
    small = inf
    index = 0
    for i in range(1,n+1):
        if time[i] < small and not visited[i]:
            small = time[i]
            index = i
    return index
        
def post(first):
    time[first] = 0
    visited[first] = True
    for j in city[first]:
        time[j[0]] = j[1]
    for i in range(n-1):
        v = smallest_node()
        visited[v] = True
        for j in city[v]:
            cost = time[v] + j[1]
            if cost < time[j[0]]:
                time[j[0]] = cost

post(c)

count = -1
for i in visited:
    if i:
        count += 1

print(count, max(time))