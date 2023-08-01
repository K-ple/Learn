answer = 0
l = map(int,input().split())
for i in l:
    answer += i ** 2
print(answer % 10)