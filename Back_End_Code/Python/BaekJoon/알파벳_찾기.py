alpabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
answer = []
word = [a for a in input()]
for i in alpabet:
    if i in word:
        answer.append(word.index(i))
    else:
        answer.append(-1)

for j in answer:
    print(j, end=' ')
