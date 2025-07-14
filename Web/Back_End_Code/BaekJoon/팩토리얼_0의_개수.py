answer = 1
for i in range(1,int(input())+1):
    answer *= i

count = 0
answer = str(answer)
for j in range(1,len(answer)+1):
    if answer[-j] == '0':
        count += 1
    else:
        break
print(count)