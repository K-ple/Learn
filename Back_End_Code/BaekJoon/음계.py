answer = []
for i in input().split():
    answer.append(int(i))
if answer == [1,2,3,4,5,6,7,8]:
    print('ascending')
elif answer == [8,7,6,5,4,3,2,1]:
    print('descending')
else:
    print('mixed')