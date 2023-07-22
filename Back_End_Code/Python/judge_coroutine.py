def calc():
    count = 0
    while True:
        x = yield count
        check = x.split()
        a, b = check[0], check[2]
        a, b = int(a), int(b)
        if '+' in check:
            count = a + b
        elif '-' in check:
            count = a - b
        elif '*' in check:
            count = a * b
        elif '/' in check:
            count = a / b

expressions = input().split(', ')
c = calc()
next(c)

for e in expressions:
    print(c.send(e))

c.close()
