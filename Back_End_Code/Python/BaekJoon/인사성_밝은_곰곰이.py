count = 0
check = {}
number = int(input())

for i in range(number):
    a = input().rstrip()
    if a == 'ENTER':
        check = {}
        continue
    if a not in check:
        count += 1
        check[a] = True

print(count)
