r = {'A+': 4.5,'A0': 4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
answer = 0
n = 0
for i in range(20):
    name, h, score = input().split()
    
    if score == 'P':
        continue
    n += float(h)
    answer +=  float(h) * r[score]

print(answer/n)
