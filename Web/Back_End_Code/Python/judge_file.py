with open('words.txt', 'r') as file:
    text = file.readline().split()
    
    #text = text.split()
    for i in text:
        
        if 'c' in i:
            print(i.strip(',.'))



        