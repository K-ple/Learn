word = input()
count = len(word)
answer = 0
while count != 0:
    a = word[-count]
    answer += 3
    if a in 'ABC':
        pass
    elif a in 'DEF':
        answer += 1
        
    elif a in 'GHI':
        answer += 2
        
    elif a in 'JKL':
        answer += 3
        
    elif a in 'MNO':
        answer += 4
        
    elif a in 'PQRS':
        answer += 5
        
    elif a in 'TUV':
        answer += 6
        
    elif a in 'WXYZ':
        answer += 7
    
    count -= 1
    
print(answer)