n = int(input())
shop = set(map(int,input().split())) #time.list < time.set 
m = int(input())
sell = list(map(int, input().split()))
for i in sell:
    if i in shop:
        print('yes',end=' ')
    else:
        print('no',end=' ')

