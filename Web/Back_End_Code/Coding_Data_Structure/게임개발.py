n, m = map(int,input().split())
a,b,d = map(int,input().split())
ma = []
answer = 1
for i in range(n):
    ma.append(list(map(int,input().split())))
ma[a][b] = 2 #2는 거쳐간 곳
while a + 1 < m and a - 1>= 0 and b + 1 <n and b-1>= 0:
    if d == 0:
        if ma[a][b-1] != 1 and ma[a][b-1] != 2 and b-1>= 0:
            ma[a][b-1] = 2
            answer += 1
            b -= 1
            d = 3
            continue
        elif ma[a+1][b] != 1 and ma[a+1][b] != 2 and a+1<n:
            ma[a+1][b] = 2
            answer += 1
            a += 1
            d = 2
            continue
        elif ma[a][b+1] != 1 and ma[a][b+1] != 2 and b+1<m:
            ma[a][b+1] = 2
            answer += 1
            b += 1
            d = 1
            continue
        elif ma[a-1][b] != 1 and ma[a-1][b] != 2 and a-1>= 0:
            ma[a-1][b] = 2
            answer += 1
            d = 0
            continue
        else:
            if ma[a+1][b] == 1:
                break
            else:
                a += 1
                continue
    
    if d == 1:
        if ma[a-1][b] != 1 and ma[a-1][b] != 2 and a-1>= 0:
            ma[a-1][b] = 2
            answer += 1
            d = 0
            continue
        
        elif ma[a][b-1] != 1 and ma[a][b-1] != 2 and b-1>= 0:
            ma[a][b-1] = 2
            answer += 1
            b -= 1
            d = 3
            continue
        elif ma[a+1][b] != 1 and ma[a+1][b] != 2 and a+1<n:
            ma[a+1][b] = 2
            answer += 1
            a += 1
            d = 2
            continue
        elif ma[a][b+1] != 1 and ma[a][b+1] != 2 and b+1<m:
            ma[a][b+1] = 2
            answer += 1
            b += 1
            d = 1
            continue
        else:
            if ma[a][b-1] == 1:
                break
            else:
                b -= 1
                continue
    if d == 2:

        if ma[a][b+1] != 1 and ma[a][b+1] != 2 and b+1<m:
            ma[a][b+1] = 2
            answer += 1
            b += 1
            d = 1
            continue
        elif ma[a-1][b] != 1 and ma[a-1][b] != 2 and a-1>= 0:
            ma[a-1][b] = 2
            answer += 1
            d = 0
            continue
        
        elif ma[a][b-1] != 1 and ma[a][b-1] != 2 and b-1>= 0:
            ma[a][b-1] = 2
            answer += 1
            b -= 1
            d = 3
            continue
        elif ma[a+1][b] != 1 and ma[a+1][b] != 2 and a+1<n:
            ma[a+1][b] = 2
            answer += 1
            a += 1
            d = 2
            continue
        else:
            if ma[a-1][b] == 1:
                break
            else:
                a -= 1
                continue
    if d == 3:

        if ma[a+1][b] != 1 and ma[a+1][b] != 2 and a+1<n:
            ma[a+1][b] = 2
            answer += 1
            a += 1
            d = 2
            continue

        elif ma[a][b+1] != 1 and ma[a][b+1] != 2 and b+1<m:
            ma[a][b+1] = 2
            answer += 1
            b += 1
            d = 1
            continue
        elif ma[a-1][b] != 1 and ma[a-1][b] != 2 and a-1>= 0:
            ma[a-1][b] = 2
            answer += 1
            d = 0
            continue
        
        elif ma[a][b-1] != 1 and ma[a][b-1] != 2 and b-1>= 0:
            ma[a][b-1] = 2
            answer += 1
            b -= 1
            d = 3
            continue
        else:
            if ma[a][b+1] == 1:
                break
            else:
                b += 1
                continue
print(answer)