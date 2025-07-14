n = 12
a = []
answer = []
for i in range(1,n+1):
        if n % i == 0:
            a.append(i)
    
for j in a:
        b = []
        for k in range(1,a+1):
            if j % k == 0:
                b.append(k)
        if len(b) == 2:
            answer.append(b[1])

print(answer)