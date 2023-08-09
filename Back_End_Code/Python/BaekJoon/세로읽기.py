li = []
answer = []
for i in range(5):
    li.append([j for j in input()])

for k in range(max([len(li[0]),len(li[1]),len(li[2]),len(li[3]),len(li[4])])):
    for j in range(5):
        try:
            answer.append(li[j][k])
    
        except IndexError:
            continue
        
print(''.join(answer))