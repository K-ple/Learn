def prime_number_generator(start, stop):
    prime_list = []
    while start <= stop:
        check = []
        for i in range(1,start+1):
            
            if start % i == 0:
                    check.append(i)
          
        if check == [1, start]:
            prime_list.append(start)
        start += 1
    yield from prime_list 

start, stop = map(int, input().split())

g= prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=' ')