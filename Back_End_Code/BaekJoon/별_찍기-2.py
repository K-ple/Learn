count = int(input())
for i in range(1,count+1):
    print('{}{}'.format(' '*(count-i),'*'*i))