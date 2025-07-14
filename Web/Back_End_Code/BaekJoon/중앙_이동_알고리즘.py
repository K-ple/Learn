g = 2
s = 2
count = int(input())

for i in range(count):
    answer = 0
    for j in range(s*2-1):
        answer += g*2-1
    g = g*2 -1
    s = s*2 -1
print(answer)