n, k = map(int,input().split())
answer = []
for i in range(1,n+1):
    if n % i == 0:
        answer.append(i)

if len(answer) < k:
    print(0)
else:
    print(answer[k-1])