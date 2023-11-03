import sys
from collections import Counter
count = int(input())

a = [int(sys.stdin.readline()) for _ in range(count)]

a.sort()

print(round(sum(a)/count))

print(a[count//2])

c = sorted(Counter(a).items(), key = lambda item: item[1])
m = c[-1][1]
count = 0
for k, v in c:
    if m == v:
        count += 1
        if count == 2:
            break
if count == 2:
    print(k)
else:
    print(c[-1][0])

print(max(a)-min(a))    