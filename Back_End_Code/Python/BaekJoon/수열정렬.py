length = int(input())
first = map(int,input().split())
number = []
check_number = []
for i in first:
    number.append(i)
    check_number.append(i)

for i in range(length):
    
    number[check_number.index(min(check_number))] = i
    check_number[check_number.index(min(check_number))] = 1001
    
for j in number:
    print(j,end=' ')
