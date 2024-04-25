dict = {'name': 'apple','type':'fruit','price': 1000}
number = ['none','name', 'type', 'price']
print('찾고 싶은 데이터의 번호를 입력해주세요')
print('1 name')
print('2 type')
print('3 price')
count = 0
def checking(a,count):
    find = int(a)


    if count == 2:
        print('3회 오류로 프로그램을 종료합니다.')
        exit()

    if find > 3 or find < 1:
        print('숫자를 잘못 입력하셨습니다')
        count += 1
        checking(input("> "),count)
    else:
        return find
find = checking(input("> "),count)

data = dict.get(number[find])
if data is None:
    print('존재하지 않는 데이터입니다.')
else:
    print('{}의 값은 {} 입니다.'.format(number[find], data))
