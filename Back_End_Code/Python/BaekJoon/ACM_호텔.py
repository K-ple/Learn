count = int(input())
answer = []

for i in range(count):
    h, w, n = map(int,input().split())
    check = 1
    for j in range(1,w+1):
        for k in range(1,h+1):
            if check == n:
                if j < 10:
                    answer.append('{}0{}'.format(k,j))
                    check = 0
                    break
                else:
                    answer.append('{}{}'.format(k,j))
                    check = 0
                    break
            else:
                check += 1
        if check == 0:
            break
for j in answer:
    print(j)