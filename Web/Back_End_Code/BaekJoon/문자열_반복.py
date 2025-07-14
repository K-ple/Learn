answer = []
count = int(input())
for i in range(count):
    re, name = input().split()
    b = []
    for j in name:
        b.append(j * int(re))
    answer.append(''.join(b))

for k in answer:
    print(k)