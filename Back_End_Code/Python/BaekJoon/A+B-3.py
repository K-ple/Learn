count = int(input())
l = []
for i in range(count):
    l.append(map(int,input().split()))
for j in l:
    print(sum(j))