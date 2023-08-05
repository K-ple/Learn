answer = []
while True:
    num = [int(i) for i in input().split()]
    if sum(num) == 0:
        break
    num.sort()
    if num[0] ** 2 + num[1] ** 2 == num[2]**2:
        answer.append('right')
    else:
        answer.append('wrong')

for j in answer:
    print(j)