num = int(input())
a =1
b =1
m = []
up = True
down = False
count = 1
while True:
    if count == num:
        print('{}/{}'.format(a,b))
        break
    if a == 1 and up:
        b += 1
        count += 1
        up = False
        down = True
        continue
    elif b == 1 and down:
        a+= 1
        count += 1
        up = True
        down = False
        continue
    else:
        if up:
            a -= 1
            b += 1
            count += 1
        if down:
            a += 1
            b -= 1
            count += 1



