#1. 디음 formatO 함수 중에서 오류가 발생하는 경우를 골라 주세요.
# 정답 3번
'''
1. "{} {}".format(52 ,573)  print: 52 573
2. "{} {}".format(52 ,type(273) print: 52 int
3. "{} {} {}".format(52, type(273)) print: IndexError
4. "{}".format(52,273) print: 52
'''

#2.  함수와 그 기능을 연결해 주세요.
fx = {'split()': 0,'upper()': 0 ,'lower()': 0,'strip()': 0}
answer = [
    "문자열을 소문자로 변환합니다.",
    "문자열을 대문자로 변환합니다.",
    "문자열 양옆의 공백을 제거합니다.",
    "문자열을 특정 문자로 자릅니다."
]
print("2번문제정답")
d = [3,1,0,2]
num = 0
for i in fx.keys():
    fx[i] = answer[d[num]]
    num += 1
for j,k in fx.items():
    print(j,k)

#3. 디음 코드의 빈칸을 채워서 실행결과처럼 출력해 보세요.

a = input("> 1번째 숫자: ") #100
b = input("> 2번째 숫자: ") #200
print()
answer = [a,b,a+b]
print('{0} + {1} = {2}'.format(answer[0],answer[1],answer[2]))
print('정답: a,b,a+b')

#4. 다음 프로그램의 실행결과를 예측해보세요.
string = "hello"
    #string. upperO 를 실행하고， string 출력하기
string.upper()
print("A 지점:", string)
    # string.upperO 실행하기
print("B 지점 :" , string.upper())
#실행결과
''' A 지점: hello
    B 지점: HELLO'''

#1. 비교 연사자를 사용한 조건식입니다. 결과가 참이면 True를, 거짓이면 False를 적어 보세요.
print(10 == 100) #False
print(10 != 100) #True
print(10 > 100) #False
print(10 < 100) #True
print(10 <= 100) #True
print(10 >= 100) #False

#2. 다음 세 개의 예제 중 "참입니다"를 출력하는 것은 몇 번 예제인가요?
#정답 3번

#1
x = 2
if x > 4:
    print("참입니다")
#2
x = 1
if x > 4:
    print("참입니다")
#3
x = 10
if x > 4:
    print("참입니다")

#3. 다음 상황들은 선택 조건으로 and 및 or 연산자를 적용하고 있습니다. 어떤 연산자가 사용 되었을까요? and 연산자라면 'a'. or 연산자라면 'o'를 괄호 안에 적어 보세요

#1
print("치킨이나 햄버거가 먹고 싶어서, 음식 주문 애플리케이션에서 치킨과 햄버거를 선택했다. {}".format('a'))
#2
print("H 브랜드가 출시한 10만원 이하의 가방을 구매하고 싶어서, H 브랜드와 10만원 이하를 조건으로 선택해서 검색했다.".format('a'))
#3
print("고궁에 입장하는데, 65세 이상의 어르신과 5살 이하의 아동은 무료 입장이었다.".format('o'))

#4. 사용자로부터 숫자 두 개를 입력받고 첫 번째 입력받은 숫자가 큰지, 두 번째 입력받은 숫자가 큰지를 구하는 프로그램을 다음 빈칸을 채워 완성해 보세요.

answer1 = 'int'
answer2 = 'int'
answer3 = 'a>b'
answer4 = 'format(a,b)'
answer5 = 'a<b'
answer6 = 'format(a,b)'

print('a = {}(input("> 1번째 숫자: "))'.format(answer1))
print('b = {}(input("> 2번째 숫자: "))'.format(answer2))
print('print()')

print('if {}:'.format(answer3))
print('    '+'print("처음 입력했던 ()가 보다 ()더 큽니다.".{})'.format(answer4))
print('if {}:'.format(answer5))
print('    '+'print("처음 입력했던 ()가 보다 ()더 큽니다.".{})'.format(answer6))


