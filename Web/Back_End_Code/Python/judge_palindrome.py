with open('words.txt', 'r') as file:
    file = file.readlines()
    for i in file:
        i.strip('\n')
        j = i(reversed=True)
        if i == j:
            print(i)