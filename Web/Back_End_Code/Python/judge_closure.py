def countdown(n):
    count = n+1
    def countd():
        nonlocal count
        count -= 1
        return count
        
    return countd
n = int(input())

c = countdown(n)
for i in range(n):
    print(c(), end=' ') 