count = int(input())
word_list = []
while count > 0:
    a = input()
    if a not in word_list:
        word_list.append(a)
    count -=1
word_list.sort()
word_list = sorted(word_list, key=len)

for i in word_list:
    print(i)