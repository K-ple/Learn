a, b = input().split()
a = int('{}{}{}'.format(a[-1],a[-2],a[-3]))
b = int('{}{}{}'.format(b[-1],b[-2],b[-3]))
print(max([a,b]))