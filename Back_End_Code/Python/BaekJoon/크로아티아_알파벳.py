word = input()
answer = 0
t = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in range(8):
    if t[i] in word:
        answer += word.count(t[i])
        word = word.replace(t[i],' ')
        
print(answer+len(''.join(word.split())))