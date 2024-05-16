import time

num = 0

target_tick = time.time() + 5
while time.time() < target_tick:
    num += 1

print(f'총 {num}번 반복하였습니다.')
