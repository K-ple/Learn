while True:
    n = int(input())
    if n == -1:
        break
    answer = []
    for i in range(1,n+1):
        if n % i == 0:
            answer.append(i)
    m = answer.pop()
    
    if sum(answer) == m:
        answer = map(str,answer)
        print('{} = {}'.format(m,' + '.join(answer)))
    else:
        print(m,'is NOT perfect.')