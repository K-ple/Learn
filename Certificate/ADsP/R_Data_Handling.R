# 데이터 이름 변경
m1 <- matrix(c(1:6), nrow=2)
colnames(m1) <- c('A', 'B', 'C')
rownames(m1) <- c('가', '나')
print(m1)
print(colnames(m1))
print(rownames(m1))

df1 <- data.frame( x = c(1, 2, 3), y = c(4, 5, 6))
colnames(df1) <- c('X', 'Y')
rownames(df1) <- c('a', 'b', 'c')
print(df1)
print(colnames(df1))
print(rownames(df1))

# 데이터 추출
v1 <- c(3, 6, 9, 12)
print(v1[2]) # 6

m1 <- matrix(c(1:6), nrow=3)
print(m1[2, 2]) # 5
colnames(m1) <- c( 'c1', 'c2')
print(m1[, 'c1']) # 1, 2, 3
rownames(m1) <- c('r1', 'r2', 'r3')
print(m1['r3', 'c2']) # 6

v1 <- c(1:6)
v2 <- c(7:12)
df1 <- data.frame(v1, v2)
# $를 사용하여 데이터 추출
print(df1$v1) # 1, 2, 3, 4, 5, 6
print(df1$v2[3]) # 9

# 데이터 결합
v1 <- c(1:3)
v2 <- c(4:6)
print(rbind(v1, v2)) # 행 결합
print(cbind(v1, v2)) # 열 결합

