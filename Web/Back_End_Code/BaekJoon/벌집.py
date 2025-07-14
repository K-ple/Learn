num = int(input())

answer = 1
check = 1
while True:
    check += 6*(answer-1)
    if check >= num:
        print(answer)
        break

    answer += 1