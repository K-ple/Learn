h = []
for i in range(9):
    h.append([int(j) for j in input().split()])
check = []
for k in h:
    check.append(max(k))
print(max(check))
print(check.index(max(check))+1, h[check.index(max(check))].index(max(h[check.index(max(check))]))+1)