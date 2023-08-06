check = []
answer = []
for i in range(28):
    check.append(int(input()))

for j in range(1,31):
    if j not in check:
        answer.append(j)
    if len(answer) == 2:
        break

print('{}\n{}'.format(answer[0],answer[1]))