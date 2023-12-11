# x - > y 값일때 x,y값 데이터 생성
x = [-3, 31, -11, 4, 0, 22, -2, -5, -25, -14]
y = [-2, 32, -10, 5, 1, 23, -1, -4, -24, -13]
print(x)
print(y)

#맷플롯립 x,y값 제공후 그래프 생성
import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show()

#x,y 값 데이터프레임 생성
import pandas as pd
df = pd.DataFrame({'X': x, 'Y': y})
print(df.shape) #10행 2열 => (10 , 2)

#데이터프레임 출력
print(df.head()) #앞에서 5개의 행을 출력
print(df.tail()) #뒤에서 5개의 행을 출력

#모델 학습에 필요한 설명 변수(X) 와 목표 변수(Y) 생성 및 데이터프레임 생성
train_features = ['X']
target_cols = ['Y']
X_train = df.loc[:, train_features]
Y_train = df.loc[:, target_cols]
print(X_train.shape, Y_train.shape)

#사이킷런 패키지에 Linear_model 모듈을 통해 모델 인스턴트 객체 생성
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
# fit 메소드를 통해 모델에 전달 및 학습 후 선형 관계식 찾음
lr.fit(X_train, Y_train)

#학습을 끝낸 모델 인스턴트 객체의 X 변수의 회귀계수(기울기) 와 상수항(Y절편) 찾는 속성
print(lr.coef_, lr.intercept_)

#X 변수의 회귀계수가 1이므로,
# lr 모델은 Y = X + 1의 관계식을 가짐
print("기울기:", lr.coef_[0][0])
print("y절편:", lr.intercept_[0])

#만들어진 학습모델에 임의 값('11')으로 Y값 예측
import numpy as np
X_new = np.array(11).reshape(1, 1) #reshape => (1행,1열) 2차원 구조로 변형
print(lr.predict(X_new))

#11부터 16까지 1씩증가하는 벡터값을 2차원 구조로 생성
X_test = np.arange(11, 16, 1).reshape(-1,1) #reshape() => -1값은 끝 n값
print(X_test)

#X_test 값을 lr 모델에 입력 후 Y_pred 값을 예측 
Y_pred = lr.predict(X_test)
print(Y_pred)