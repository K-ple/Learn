count = int(input())
answer = []

for i in range(count):
    check = []
    ox = input()
    o = 0
    for j in ox:
        if j == 'O':
            o += 1
            check.append(o)
        else:
            o = 0
    
    answer.append(sum(check))
for j in answer:
    print(j)