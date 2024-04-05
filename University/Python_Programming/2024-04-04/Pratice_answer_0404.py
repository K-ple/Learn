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

a = input("> 1번째 숫자: ")
b = input("> 2번째 숫자: ")
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



