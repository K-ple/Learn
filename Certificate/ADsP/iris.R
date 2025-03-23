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
copy_iris <- iris
print(dim( copy_iris ))
copy_iris[ sample(1:150, 30), 1] <- NA
copy_iris <- copy_iris[complete.cases(copy_iris), ]
print(dim( copy_iris ))
#-------------------------------------------
# 2. 평균 대치법
copy_iris <- iris
copy_iris[ sample(1:150, 30), 1] <- NA

meanValue <- mean(copy_iris$Sepal.Length, na.rm = TRUE) # 결측값을 제외한 평균 계산
copy_iris$Sepal.Length[is.na(copy_iris$Sepal.Length)] <- meanValue # 평균 대치
print(missmap(copy_iris))

#centralImputation 함수를 이용한 평균 대치법
library(DMwR2)
copy_iris <- iris
copy_iris[ sample(1:150, 30), 1] <- NA
copy_iris <- centralImputation(copy_iris)
print(missmap(copy_iris))
#-------------------------------------------
# 3. 단순 확률 대치법
# K-Nearst Neighbor(KNN) 알고리즘을 이용한 결측값 대치
copy_iris <- iris
copy_iris[ sample(1:150, 30), 1] <- NA
copy_iris <- knnImputation(copy_iris, k = 10)
print(missmap(copy_iris))
#-------------------------------------------
# 4. 다중 대치법
copy_iris <- iris
copy_iris[ sample(1:150, 30), 1] <- NA
library(Amelia)
iris_imp <- amelia(copy_iris, m=3, cs = 'Species')
copy_iris$Sepal.Length <- iris_imp$imputations[[3]]$Sepal.Length
print(missmap(copy_iris))
#-------------------------------------------

# 이상값
# 사분위수 범위(IQR)를 이용한 이상값 탐지
data <- c(3, 10, 13, 16, 11, 20, 17, 25, 43)
boxplot(data, horizontal = TRUE)
#-------------------------------------------
