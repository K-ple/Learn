count = int(input())
a = []
for i in range(count):
    a.append(input().split())
for j in range(count):
    print('Case #{}: {} + {} = {}'.format(j+1,a[j][0],a[j][1],sum(map(int, a[j]))))