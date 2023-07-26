'''answer = []
for i in range(int(input())):
    a,b = map(int,input().split())
    answer.append(a+b)

for j in answer:
    print(j)'''

import sys
line = []
b = int(input())
for i in range(b):
    line.append(sys.stdin.readline())

for j in line:
    print(sum(map(int, j.split())))