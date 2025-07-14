def setting(data):
    return data[1]
count = int(input())
answer = []
for i in range(count):
    k , v = input().split()
    answer.append([k,int(v)])
answer = sorted(answer, key=setting)
for j in answer:
    print(j[0], end=' ')