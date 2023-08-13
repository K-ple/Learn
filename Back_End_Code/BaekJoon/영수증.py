end_money = int(input())
j = int(input())
while j != 0:
    a, b = map(int, input().split())
    end_money -= a*b
    j -= 1

if end_money == 0:
    print('Yes')
else:
    print('No')