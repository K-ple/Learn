count = int(input())
a = []
while count != 0:
    a.append(map(int,input().split()))
    count -= 1

for i in range(len(a)):
    print('Case #{}: {}'.format(i+1,sum(a[i])))