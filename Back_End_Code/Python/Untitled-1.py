st = input()
checklist = []
for i in range(st):
    
    if st[i] in checklist:
        checklist = [] 
    if checklist == None:
        checklist.append(st[i])
    
    