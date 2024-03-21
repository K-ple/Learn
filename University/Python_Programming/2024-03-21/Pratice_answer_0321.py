#1. 다음은 변수에 값을 할당하기 위한 구문입니다. 빈칸에 알맞은 기호를 써 보세요.
answer = '='
print('변수 이름',answer,"값")

print()
#2. 다음은 숫자에 적용할 수 있는 복합 대입 연산자입니다. 설명을 보고 왼쪽 연산자 항목에 기호를 써 보세요.
a_1 = '+='
a_2 = '-='
a_3 = '*='
a_4 = '/='
a_5 = '%='
a_6 = '**='

print(a_1,': 숫자 덧셈 후 대입.')
print(a_2,': 숫자 뺄샘 후 대입.')
print(a_3,': 숫자 곱셈 후 대입.')
print(a_4,': 숫자 나눗셈 후 대입.')
print(a_5,': 숫자 나머지 구한 후 대입.')
print(a_6,': 숫자 제곱 후 대입.')

print()
#3. 문자열을 숫자로 변환하는 함수, 숫자를 문자열로 변환하는 함수입니다. 설명을 보고 알맞은 함수 이름을 넣어 보세요.
a_1 = 'int()'
a_2 = 'float()'
a_3 = 'str()'
print(a_1,": 문자열을 int 자료형으로 변환")
print(a_2,": 문자열을 float 자료형으로 변환")
print(a_3,": 숫자를 문자열로 변환")

print()
#4. 다음코드는 inch 단위의 자료를 입력받아 cm 단위를 구하는 예제입니다. 빈칸에 알맞은 내용을 넣어 코드를 완성해 주세요.
a_1 = 'input'
a_2 = 'int'
print('str_input = {}("숫자 입력> ")'.format(a_1))
print('num_input = {}(str_input)'.format(a_2))

print()
#5. 원의 반지름을 입력받아 원의 둘레와 넓이를 구하는 코드입니다. 빈칸에 알맞은 내용ㅇ을 넣어 코드를 완성해 주세요.
a_1 = 'input'
a_2 = 'int'
a_3 = 'num_input'
a_4 = 'num_input'
print('str_input = {}("숫자 입력> ")'.format(a_1))
print('num_input = {}(str_input)'.format(a_2))
print('print()')
print('print("반지름:", num_input)')
print('print("둘레:", 2 * 3.14 * {})'.format(a_3))
print('print("넓이:", 3.14 * {} ** 2)'.format(a_4))

print()
#6. 프로그램을 실행했을 때 문자열 두 개를 입력받고 다음과 같이 출력하는 프로그램이 있다고 가정합시다. 굵은 글씨로 되어 있는 부분은 사용자 입력입니다.
user_input_1 = '안녕하세요'
user_input_2 = '아침입니다'

print('a = input("문자열 입력> ")')
print('b = input("문자열 입력> ")')

print('print(a, b)')
#정답
swap_keyword = user_input_1
user_input_1 = user_input_2
user_input_2 = swap_keyword

print(user_input_1, user_input_2)

