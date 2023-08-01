answer = 'a'
name = input().upper()
check = list(set(i for i in name))
for i in check:
    if name.count(i) == name.count(answer):
        button = 0
    if name.count(i) > name.count(answer):
        answer = i
        button = 1
if button:
    print(answer)
else:
    print('?')