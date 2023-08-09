count = int(input())
for i in range(1,count+1):
    print('{}{}'.format(' '*(count-i),'*'*((2*i)-1)))
for j in range(1, count):
    print('{}{}'.format(' '*j,'*'*((count-j)*2-1)))