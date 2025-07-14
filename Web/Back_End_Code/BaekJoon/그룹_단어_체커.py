count = int(input())
answer = 0
li = []
for i in range(count):
    li.append(input())

for j in li:
    check = []
    c = 0
    for k in j:
        if c != k:
            if k not in check:
                check.append(c)
            else:
                answer -= 1
                break
        
        else:
            continue

        
        c = k
    answer += 1

print(answer)
        