n = int(input())
count = 0
l = [n]
while 1 not in l:
    mid = []
    for i in l:
        if i % 5 == 0:
            mid.append(i//5)
        if i % 3 == 0:
            mid.append(i//3)
        if i % 2 == 0:
            mid.append(i//2)
        if i>1:
            mid.append(i-1)
    l = mid
    count += 1

print(count)