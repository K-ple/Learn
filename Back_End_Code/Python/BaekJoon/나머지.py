answer = []
for i in range(10):
    a = int(input()) % 42
    if a not in answer:
        answer.append(a)

print(len(answer))