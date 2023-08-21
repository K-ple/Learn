n = int(input())
answer = 0
for i in range(n+1):
    if i == 3:
        answer+= 3600
        continue
    for j in range(60):
        if '3' in str(j):
            answer += 60
        else:
            answer += 15

print(answer)