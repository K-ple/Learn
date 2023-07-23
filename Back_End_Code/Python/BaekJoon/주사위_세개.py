f, s, t = map(int, input().split())
if f == s and s == t:
    print(10000 + f*1000)
elif f == s or s == t:
    print(1000 + s * 100)
elif f == t:
    print(1000 + f*100)
else:
    print(max([f,s,t])*100)