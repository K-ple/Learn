x, y = map(int, input().split())


def calc(x,y):
    return x+y, x-y, x*y, x/y

a, s, m, d =calc(x,y)
print('{0},{1},{2},{3}'.format(a,s,m,d))
