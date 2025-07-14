count = int(input())
if count == 1:
    print(int(input())**2)
    exit()
a = map(int,input().split())
yak = []
for i in a:
    yak.append(i)
print(min(yak)*max(yak))