n = int(input())
before = []
after = []
for i in input().split():
    before.append(int(i))
m = max(before)    
for j in range(n):
    after.append(before[j]/m*100)

print(sum(after)/n)
