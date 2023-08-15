number, jin = map(int,input().split())
d = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = ''
while number > 0:
    a = number % jin
    answer = d[a] + answer
    number //= jin

print(answer)