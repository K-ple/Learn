count = int(input())
answer = []
for i in range(count):
    answer.append(int(input()))
answer.sort(reverse=True)
for j in answer:
    print(j, end=' ')