n, x = map(int, input().split())
answer = []
num = [int(i) for i in input().split()]
for j in num:
    if j < x:
        answer.append(j)

for k in answer:
    print(k, end=' ')