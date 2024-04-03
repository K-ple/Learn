def first_input():
    while True:
        text_number = input("계산식을 입력해주세요.\n숫자와 등호 및 수식 사이에 공백이 있어야 됩니다.: ").split()
        #등호 존재 확인
        if '=' in text_number:
            return text_number
        elif text_number.count('=') > 1:
            print('등호는 하나만 넣어 주세요.')
        else:
            print('등호를 넣어 주세요.')

sik = first_input()
math = ['+', '-','*','/']
# True: 숫자 , False: 수식 또는 등호
# 처음은 answer 값에 넣기위해 False 처리
button_next = False
answer = 0
for i in sik:
    if button_next:
        try:
            a = int(i)
            if check_math:
                if check_math == '+':
                    answer += a
                elif check_math == '-':
                    answer -= a
                elif check_math == '*':
                    answer *= a
                else:
                    answer /= a

                check_math = None
            button_next = False
        #숫자 다음에 수식이나 등호가 오는지 확인
        except ValueError:
            print("제대로 된 식이 아닙니다. 프로그램을 종료 합니다.")
            exit()

    else:
        if i in math:
            if i == '+':
                check_math = '+'
            elif i == '-':
                check_math = '-'
            elif i == '*':
                check_math = '*'
            else:
                check_math = '/'
        elif i == '=':
            break
        else:
            answer += int(i)
            continue
        button_next = True

print('식의 결과는: {} 입니다'.format(answer))
