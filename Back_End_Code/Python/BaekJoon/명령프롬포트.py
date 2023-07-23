count = int(input())
a = []
answer = []
co = 0
for i in range(count):
    a.append(input())
if count == 1:
    print(a[0])
    exit()
for j in range(len(a[0])):
    for k in range(count-1):
        if a[k][j] == a[k+1][j]:
            co = 1
        else:
            co = 0
            break
    if co == 1 :
        answer.append(a[0][j])
    else:
        answer.append('?')

print(''.join(answer))