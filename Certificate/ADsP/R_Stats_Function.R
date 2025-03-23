#숫자 연산
print(sqrt(2)) # 제곱근
print(abs(-3)) # 절대값
print(exp(1)) # 지수
print(log(2)) # 자연로그
print(log10(100)) # 상용로그
print(pi) # 원주율
print(round(3.141592, 2)) # 반올림
print(ceiling(3.141592)) # 올림
print(floor(3.141592)) # 내림
#-------------------------------------------

#문자 연산
data <- 'This is a pen'
print(data)
print(tolower(data)) # 소문자로 변경
print(toupper(data)) # 대문자로 변경
print(nchar(data)) # 문자열 길이
print(substr(data, 1, 4)) # 문자열 자르기
print(strsplit(data, ' ')) # 문자열 나누기
print(grepl('This', data)) # 문자열 포함 여부
print(gsub('This', 'That', data)) # 문자열 변경
#-------------------------------------------

#벡터 연산
v1 <- c(1:5)
v2 <- c(6:10)
print(length(v1)) # 벡터 길이
print(paste(v1, collapse=' ')) # 벡터 출력
print(cov(v1, v2)) # 공분산
print(cor(v1, v2)) # 상관계수
print(table(v1)) # 빈도수 (데이터의 개수)
print(order(v1)) # 순위
#-------------------------------------------

#행렬 연산
m1 <- matrix(c(1:6), nrow=2)
m2 <- matrix(c(7:12), ncol=2)
print(t(m1)) # 전치행렬
print(diag(m1)) # 대각행렬
print(m1 %*% m2) # 행렬곱

#데이터 탐색
x <- c(1:12)

print(head(x, 5)) # 앞에서 5개
print(tail(x, 5)) # 뒤에서 5개
print(quantile(x)) # 사분위수
#-------------------------------------------

#데이터 전처리
df1 <- data.frame( x = c(1, 1, 1, 2, 2), y = c(2, 3, 4, 3, 3))
df2 <- data.frame( x = c(1:4), z = c(5:8))
print(df1)
print(df2)
print(subset(df1, x == 1)) # 조건에 맞는 데이터 추출

print(merge(df1, df2, by=c('x'))) # 데이터 결합

# 1은 행, 2는 열
print(apply(df1, 1, sum)) # 행 합계
print(apply(df1, 2, sum)) # 열 합계
#-------------------------------------------

#정규분포(기본값은 평균 0, 표준편차 1)
print(dnorm(0)) # 확률밀도함수
print(rnorm(5)) # 난수 생성
print(pnorm(0)) # 누적분포함수
print(qnorm(0.5)) # 분위수
#-------------------------------------------

#표본추출
print(runif(5)) # 균일분포
print(sample(1:10, 5)) # 샘플링
#-------------------------------------------

#날짜
print(Sys.Date()) # 현재 날짜
print(Sys.time()) # 현재 시간
print(as.Date('2021-01-01')) # 날짜 변환
print(format(Sys.Date(), '%Y-%m-%d')) # 날짜 형식
print(unclass(Sys.time())) # 숫자로 변환
print(as.POSIXct(Sys.time())) # POSIXct 형식
#-------------------------------------------

#산점도
x <- c(1:10)
y <- rnorm(10)
plot(x, y, type='l', xlim= c(-2,12), ylim=c(-2,12), xlab='X axis', ylab='Y axis', main='Test Plot')
#-------------------------------------------

#파일 읽기 쓰기
#read.csv('data.csv') # csv 파일 읽기
#write.csv(df1, 'data.csv') # csv 파일 쓰기
#saveRDS(df1, 'data.rds') # RDS 파일 쓰기
#readRDS('data.rds') # RDS 파일 읽기
#-------------------------------------------

#기타
#install.packages('ggplot2') # 패키지 설치 (install 패키지)
#library(ggplot2) # 패키지 로드 (import 패키지)
#getwd() # 현재 작업 디렉토리
#setwd('C:/Users') # 작업 디렉토리 변경
