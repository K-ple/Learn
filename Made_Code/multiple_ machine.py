
import random
i = 0 #문제관련 while 키
how = 1 #다시하기 관련 while 키
x = None #처음 키는 가지고 있지 않으나 한번이라도입력시에는 elif 문으로 넘어감
pr = 0 #프로그램 온으프  (아직은 테스트용) 
while pr == 0:
    m1 = random.randint(1, 9)
    m2 = random.randint(1, 9) #자동 숫자 배정       
        
    i = 0
    while i == 0:
        if x is None: 
            a = input(str(m1) + 'x' + str(m2) + '의 답을 입력하세요: ')
            
        elif not x is None:  
            a = input('다시 입력해주세요! : ')

        try:
            a = int(a)    
        except ValueError:
            print('정수를 입력해주세요!')
            x = 1
            continue
        if a == m1 * m2:
            print('정답입니다!')
            how = 1
            i = 1
            
            
            while how == 1:
                how = input('다음 문제를 푸시겠습니까? (Y/N) : ')
                if how == 'Y' or how == 'y':
                    x = None

                elif how == 'N' or how == 'n':
                    print('프로그램을 종료합니다.')
                    exit()
                else:
                    how = 1
                    x = None 
        else:
            x = 1    
            
