n = int(input())
a, b = 1, 1
l = list(input().split())
for i in l:
    if i == 'L':
        b -= 1
    elif i == "R":
        b += 1
    elif i == "U":
        a -= 1
    else:
        a += 1
    if not(a > 0 and a <= n):
        if a == 0:
            a += 1
        else:
            a -= 1
    if not(b > 0 and b <= n):
        
        if b == 0:
            b += 1
        else:
            b -= 1
print(a,b)