#character
print('character')
print('-----------------')
print(class('abc'))
print(class("abc"))
print(class('1'))
print(class('TRUE'))
print('-----------------')
print('')

#numeric
print('numeric')
print('-----------------')
print(class(1))
print(class(Inf))
print(class(-3))
print('-----------------')
print('')

#logical
print('logical')
print('-----------------')
print(class(TRUE))
print(class(FALSE))
print('-----------------')
print('')

#NULL
print('NULL')
print('-----------------')
print(class(NULL))
print('-----------------')
print('')

#연산자
print('대입 연산자')
print('-----------------')
string1 <- 'abc'
'data' -> string2
number1 <<- 15
Inf ->> number2
logical = NA 

print(string1)
print(string2)
print(number1)
print(number2)
print(logical)

print('-----------------')
print('')

print('비교 연산자')
print('-----------------')
print(string1 == 'abc') #같다
print(string1 != 'abcd') #같지 않다
print(string2 > 'DATA') #대문자가 소문자보다 작다
print(number1 <= 15) #같거나 작다
print(is.na(logical)) #NA는 is.na로 확인
print(is.null(NULL)) #NULL은 is.null로 확인
print('-----------------')
print('')

print('산술 연산자')
print('-----------------')
print(1 + 2) #더하기
print(3 - 4) #빼기
print(5 * 6) #곱하기
print(7 / 8) #나누기
print(9 %/% 3) #// 몫
print(9 %% 3) #나머지
print(2 ^ 3) #제곱
print(2 ** 2) #제곱
print(exp(1)) #지수
print('-----------------')
print('')

print('기타 연산자')
print('-----------------')
print(!TRUE) #NOT
print(TRUE & FALSE) #AND
print(TRUE | FALSE) #OR
print('-----------------')
print('')