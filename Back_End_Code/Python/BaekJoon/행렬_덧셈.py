n, m = map(int,input().split())
first = []
second = []
for i in range(n):
    first.append([int(j) for j in input().split()])

for k in range(n):
    second.append([int(l) for l in input().split()])

for o in range(n):
    for p in range(m):
        print(first[o][p] + second[o][p], end=' ')

    print('')