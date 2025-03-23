# 기본함수

#help(), ?
#help(paste) # paste 함수 도움말
#?paste # paste 함수 도움말

print(paste('This is', 'a pen')) # 문자열을 이어 붙이는 함수

print(seq(1, 10, by=2)) # 1부터 10까지 2씩 증가하는 수열 생성

print(rep(1,5)) # 1을 5번 반복

a <- 1
print(a)
rm(a) # 변수 삭제
# print(a) # 변수가 삭제되어 에러 발생

print(ls()) # 현재 환경에 있는 변수 목록

print(10) # 출력 함수
# -------------------------------------------

# 통계 함수
v1 <- c(1:9)
print(sum(v1)) # 합계
print(mean(v1)) # 평균
print(median(v1)) # 중앙값
print(var(v1)) # 분산
print(sd(v1)) # 표준편차
print(max(v1)) # 최대값
print(min(v1)) # 최소값
print(range(v1)) # 범위
print(summary(v1)) # 요약 통계량
# -------------------------------------------

# 왜도 및 점도
#nstall.packages('fBasics')
#library(fBasics)

print(skewness(v1)) # 왜도
print(attr(, "method")) # 왜도 계산 방법
print(kurtosis(v1)) # 점도
print(attr(, "method")) # 점도 계산 방법
# -------------------------------------------