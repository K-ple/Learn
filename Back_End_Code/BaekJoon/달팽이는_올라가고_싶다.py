a, b, v = map(int, input().split())

days = (v - a) // (a - b)
if (v - a) % (a - b) == 0:
    days += 1
else:
    days += 2

print(days)
