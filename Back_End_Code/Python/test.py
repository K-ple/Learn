#col, row = map(int, input().split())  #가로세로크기입력
first = input()  #첫번째 줄 
second = input()
third = input()
gs = ([-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1])
#나중에 삭제 할것!
col, row = 3, 3
first = '.**'
second = '*..'
third = '.*.'

fl = []  #첫번째 줄 리스트
sl = []
tl = []

for f in range(len(first)):
    
    fv  = first[f] #fv = first value
    fl.append(fv)
    
for s in range(len(second)):
    
    sv = second[s]
    sl.append(sv)

for t in range(len(third)):
    
    tv = third[t]
    tl.append(tv)

mine = [fl,sl,tl] #줄 리스트 묶기용
for i in range(col):
    for j in range(row):
    
        if mine[i][j] == '.':
            mine[i][j] = 0
            for k in range(-1,2):
                for l in range(-1,2):
                    if i+k <= 0 and j+l <= 0:
                        if i !=0 and j !=0 and i !=col-1 and j != row-1:
                            if mine[i+k][j+l] == '*':
                                mine[i][j] += 1
                        elif i in range(1,row-1):
                              if mine[i+k][j+l] == '*':
                                mine[i][j] += 1
                    
                
for m in range(col):
    for n in range(row):           
        print(mine[m][n], end='')

    print()