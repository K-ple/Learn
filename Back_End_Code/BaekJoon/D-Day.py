from datetime import datetime

fy, fm, fd = map(int,input().split())
sy, sm, sd = map(int,input().split())
first = datetime(fy,fm,fd)
second = datetime(sy,sm,sd)
answer = second - first
if sy > fy+1000 or (fy+1000 == sy and sm> fm) or (fy+1000 == sy and sm == fm and sd >= fd):
    print('gg')
    
else:
    print('D-{}'.format(answer.days))