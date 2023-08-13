start_h , start_m = map(int,input().split())
oven_time = int(input())
start_h += oven_time//60
start_m += oven_time % 60
if start_m >= 60:
    start_h += start_m // 60
    start_m = start_m % 60
if start_h >= 24:
    start_h -= 24
print(start_h, start_m)