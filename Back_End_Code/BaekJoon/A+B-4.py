import sys
answer = []
while True:
    a = sys.stdin.readline()
    if a == '':
        break
    else:
        answer.append(sum(map(int,a.split())))
    
for i in answer:
    print(i)