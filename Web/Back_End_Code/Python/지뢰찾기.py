col, row = map(int,input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))

for j in range(col):
    for k in range(row):
        if matrix[j][k] == '.':
            matrix[j][k] = 0
            for l in range(-1,2):
                for m in range(-1,2):
                    if 0 <= j+l <= row-1  and 0 <= k+m <= col-1:
                        if matrix[j+l][k+m] == '*':
                            matrix[j][k] += 1

for o in matrix:
    for p in o:
        print(p, end='')
    print()