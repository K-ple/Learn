count = int(input())
chong = ['ChongChong']
answer = 0
for _ in range(count):
    a, b = input().split()

    if a in chong and b not in chong:
        chong.append(b)
        answer += 1
    elif b in chong and a not in chong:
        chong.append(a)
        answer += 1

print(len(chong))