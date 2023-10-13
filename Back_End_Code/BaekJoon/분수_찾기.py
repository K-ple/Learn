num = int(input())
ex = 1

while num > ex:
    num -= ex
    ex += 1

if ex % 2 == 0:
    a = num
    b = ex - num + 1
else:
    b = num
    a = ex - num + 1


print('{}/{}'.format(a,b))
