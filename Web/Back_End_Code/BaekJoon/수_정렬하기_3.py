import sys
num = int(input())
answer = dict()
for _ in range(num):
    a =int(sys.stdin.readline())
    if a not in answer:
        answer[a] = 1
    else:
        answer[a] += 1

an = dict(sorted(answer.items()))

for k, v in an.items():
    for _ in range(v):
        print(k)
    