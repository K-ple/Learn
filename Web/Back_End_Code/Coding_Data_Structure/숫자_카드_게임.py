n, m = map(int,input().split())
answer = []
for i in range(n):
    li = list(map(int,input().split()))
    answer.append(min(li))

print(max(answer))