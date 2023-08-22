n = input()
number = {'a':1, 'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
first = number[n[0]]
second = int(n[1])
count = 0
if first - 2 > 0:
    if second - 1 > 0:
        count += 1
    if second + 1 < 9:
        count += 1
if first + 2 < 9:
    if second - 1 > 0:
        count += 1
    if second + 1 < 9:
        count += 1

if second - 2 > 0:
    if first - 1 > 0:
        count += 1
    if first + 1 < 9:
        count += 1
if second + 2 < 9:
    if first - 1 > 0:
        count += 1
    if first + 1 < 9:
        count += 1

print(count)