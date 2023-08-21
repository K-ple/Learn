n, k = map(int,input().split())
answer = 0
while n != 1:
    if n % k == 0:
        n /= k
    else:
        n -= 1
    answer += 1
print(answer)