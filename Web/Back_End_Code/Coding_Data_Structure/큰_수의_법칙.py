n, m, k = map(int,input().split())
answer = []
num = list(map(int,input().split()))
num.sort()
num.reverse()
count = 0

while len(answer) < m:
    if count < k:
        answer.append(num[0])
        count += 1
    else:
        count = 0
        answer.append(num[1])

print(sum(answer))