squard = [[0]*101 for i in range(101)]
answer = 0
count = int(input())
m = []
for _ in range(count):
    a, b = map(int,input().split())
    m.append([a,b])

for i in m:
    for j in range(i[1],i[1]+10):
        for k in range(i[0],i[0]+10):
            
            squard[j][k] = 1

for n in squard:
    answer += n.count(1)

print(answer)