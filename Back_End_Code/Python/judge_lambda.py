files= input().split()
print(list(map(lambda x: '00'+ x if len(x.split('.')[0]) == 1 else '0'+x if len(x.split('.')[0]) == 2 else x,files)))