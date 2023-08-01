answer = 1
for i in range(3):
    answer *= int(input())
answer = str(answer)
for j in range(10):
    print(answer.count(str(j)))