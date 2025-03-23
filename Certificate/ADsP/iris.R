# iris 데이터셋 불러오기
print(head(iris, 3))
#-------------------------------------------

# 기초 통계량
print(summary(iris))
#-------------------------------------------

# 데이터 구조 파악
print(str(iris))
#-------------------------------------------

# Amelia 패키지를 이용한 결측값 시각화
#install.packages("RcppArmadillo", type = "source")
#install.packages("Amelia", type = "source")
library(Amelia)
copy_iris <- iris
copy_iris[ sample(1:150, 15), 1] <- NA
missmap(copy_iris, main='Missing Map', col=c('yellow', 'black'), legend=FALSE)
#-------------------------------------------

# 결측값 대치 방법
#-------------------------------------------
# 1. 단순 대치법