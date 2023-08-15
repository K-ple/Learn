count = int(input())
answer = []
for i in range(count):
    r = []
    change = int(input())
    r.append(change // 25)
    change %= 25
    r.append(change // 10)
    change %= 10
    r.append(change//5)
    r.append(change % 5)
    answer.append('{} {} {} {}'.format(r[0],r[1],r[2],r[3]))

for j in answer:
    print(j)