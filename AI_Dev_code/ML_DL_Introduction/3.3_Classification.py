import pandas as pd
import numpy as np 
from sklearn import datasets

#iris(붓꽃) 데이터셋 로딩
iris = datasets.load_iris()

print(iris.keys())

#데이터셋 설명(DESCR{Description}) 출력
print(iris['DESCR'])

#데이터셋 크기, 데이터셋 내용(0,1,2 클래스) 출력
print('데이터셋 크기:', iris['target'].shape)
print('데이터셋 내용:\n', iris['target'])

#데이터의 구분 기준(속성)[꽃받침의 길이와 폭, 꽃잎의 길이와 폭] 출력 (첫번째부터 7번째까지만 출력)
print('데이터셋 크기:', iris['data'].shape)
print('데이터셋 내용:\n', iris['data'][:7, :])

#data 속성을 데이터프레임(표 형태)으로 변환
df = pd.DataFrame(iris['data'], columns=iris['feature_names'])
print('데이터프레임의 형태:', df.shape)
print(df.head)

#데이터프레임 열이름 지정
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
print(df.head(2)) #2번째 데이터까지만 출력

#데이터 프레임 열 추가 (가장 오른쪽 열)
df['Target'] = iris['target'] # Target 이름의 열을 생성 및 나열 (class: 0, 1, 2)
print('데이터셋의 크기:', df.shape)
print(df.head())

#데이터프레임의 기본 정보를 출력 (150개의 데이터를 소유하며 , Target 열을 제외하고는 모두 소수형(float))
print(df.info())

#데이터 프레임의 통계정보를 출력
print(df.describe())

#데이터프레임의 결측값  확인 (0일경우 정상데이터, 1일경우 결측값)
print('결측값 확인:\n',df.isnull().sum()) #결측값: 자료를 수집하는데 실패했거나 정리하는 과정에서 누락되어 유효한 데이터가 없는 경우

#중복 데이터 확인 (각 행 샘플 데이터가 이전 행의 데이터와 중복되면 True(1) 그렇지 않으면 False(0))
print('중복데이터 확인:',bool(df.duplicated().sum()),df.duplicated().sum()) 

#중복 데이터 출력
print(df.loc[df.duplicated(), :]) #142번 데이터와 그 이전 (>142) 데이터 중 중복이 있음을 알 수 있음

#중복 데이터 모두 출력
print(df.loc[(df.sepal_length==5.8)&(df.petal_width==1.9), :]) #142번 데이터의 일부 값과 동일한 값을 가진 데이터를 찾은후 모두 나열

#중복 데이터 제거
print('\n중복 데이터 제거')
df = df.drop_duplicates()
print(df.loc[(df.sepal_length==5.8)&(df.petal_width==1.9), :]) #위 값과 동일한 데이터가 101만 남으므로 동일했던 142번 데이터가 삭제된 것을 알 수 있음

#변수 간의 상관 관계 분석 (절대값이 1에 가까울 수록 상관 관계가 높음)
print(df.corr())

#시각화 라이브러리 불러오기
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font_scale=1.2) #시본의 글씨 크기 배율을 1.2배로 설정

#상관 계수 히트맵 설정 및 출력
sns.heatmap(data=df.corr(), square=True, annot=True, cbar=True) #annot: 상관 계수 숫자 표시여부, cbar: 그라데이션바 표시여부 
plt.show()

#Target 열에 있는 각 클래스별 갯수 출력
print(df['Target'].value_counts())

#sepal_length 값의 분포 그래프 출력
plt.hist(x='sepal_length', data=df)
plt.show()

#sepal_width 값의 분포를 시본 displot 함수를 이용하여 히스토그램 형태의 그래프를 출력
sns.displot(x='sepal_width', kind='hist', data=df) #kind="hist" : 히스토그램으로 출력
plt.show()

#petal_width 값의 분포를 kde 밀도 함수 그래프로 출력
sns.displot(x='petal_width', kind='kde', data=df)
plt.show()

#sepal_length 값의 'Target'열의 품종(0,1,2)별로 구분한 분포를 kde 밀도 함수 그래프로 출력
sns.displot(x='sepal_length',hue='Target' ,kind='kde', data=df) #hue옵션을 통해 지정 열의 데이터 그래프를 모두 나열
plt.show()

#위 sepal_length값을 제외한 나머지 값들을 한번에 그래프로 출력
for col in ['sepal_width', 'petal_length', 'petal_width']:
    sns.displot(x=col, kind='kde', hue='Target', data=df)
plt.show()

#서로 다른 피처 간 관계를 나타내는 kde 밀도 함수 그래프를 출력
sns.pairplot(df, hue='Target', size= 2.5, diag_kind= 'kde')
plt.show() # 대각 방향에는 밀도함수로 나타남


from sklearn.model_selection import train_test_split

X_data = df.loc[:, 'sepal_length': 'petal_width']
Y_data = df.loc[:, 'Target']
X_train, X_test, Y_train, Y_test = train_test_split(X_data, Y_data, #80% 데이터는 train, 20% 데이터는 test 데이터로 분할 
                                                    test_size= 0.2, #전체 데이터중 20%를 테스트 데이터로 분할 사용 (나머지 80%는 훈련용 데이터로 사용)
                                                     shuffle=True, #무작위로 섞어서 추출
                                                       random_state=20) #항상 일정한 기준으로 무작위 분할

print(X_train.shape, Y_train.shape)
print(X_test.shape, Y_test.shape)

#KNN 분류 알고리즘
#기존 데이터 중 속성이 비슷한 7개(n_neighbors=7)의 이웃 찾기
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train, Y_train)

#X_test의 데이터 중 처음 5개의 데이터의 예측값을 출력
Y_knn_pred = knn.predict(X_test)
print("예측값:", Y_knn_pred[:5])

#예측값(knn_pred)과 정답 레이블(Y_test)을 비교하여 모델예측의 정확도(성능)을 파악
from sklearn.metrics import accuracy_score
knn_acc = accuracy_score(Y_test, Y_knn_pred)
print('Accuracy:%.4f'% knn_acc) #약 96.67%의 정확도를 보임


#SVM 분류 알고리즘
#모델학습
from sklearn.svm import SVC
svc = SVC(kernel='rbf')
svc.fit(X_train, Y_train)

y_svc_pred = svc.predict(X_test)
print("예측값:", y_svc_pred[:5])

#정확도(성능)을 파악
svc_acc = accuracy_score(Y_test,y_svc_pred)
print('Accuracy:%.4f'% svc_acc) #SVM모델은 검증 데이터(X_test)에 대하여 100%의 정확도를 보이는 것을 알 수있음


#로지스틱 회귀 분류 알고리즘
#모델학습
from sklearn.linear_model import LogisticRegression
lrc = LogisticRegression()
lrc.fit(X_train,Y_train)

#X_test의 데이터 중 처음 5개의 데이터의 예측값을 출력
y_lrc_pred = lrc.predict(X_test)
print("예측값:", y_lrc_pred[:5])

#정확도(성능)을 파악
lrc_acc = accuracy_score(Y_test,y_lrc_pred)
print('Accuracy:%.4f'% lrc_acc) #LRC모델은 SVM 모델과 동일하게 100%의 정확도를 보이는 것을 알 수있음

#확률값 예측
y_lrc_prob = lrc.predict_proba(X_test)
print(y_lrc_prob) #첫 번쨰 열부터 각각 0,1,2 클래스의 예측확률을 나타내며 0번째 열의 확률이 98%(9.83094453e-01 = 0.98..)로 가장 크기 때문에 첫 번째 샘플은 클래스 0으로 분류됨


#의사결정나무 분류 알고리즘
#모델학습
from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier(max_depth=3, random_state=20) #max_depth: 트리의 최대 깊이
dtc.fit(X_train, Y_train)

#X_test의 데이터 중 처음 5개의 데이터의 예측값을 출력
y_dtc_pred = dtc.predict(X_test)
print("예측값:", y_dtc_pred[:5])

#정확도(성능)을 파악
dtc_acc = accuracy_score(Y_test,y_dtc_pred)
print('Accuracy:%.4f'% dtc_acc) #약 93.33% 의 정확도를 보임

#앙상블모델

#Voting
#Hard Voting 모델 학습
from sklearn.ensemble import VotingClassifier 
hvc = VotingClassifier(estimators=[('KNN', knn),('SVM', svc),('DT',dtc)],
                       voting='hard') #3개 모델이 예측한 값 중 다수결로 최종 분류 클래스를 정함
hvc.fit(X_train,Y_train)

#X_test의 데이터 중 처음 5개의 데이터의 예측값을 출력
y_hvc_pred = hvc.predict(X_test)
print("예측값:", y_hvc_pred[:5])

#정확도(성능)을 파악
hvc_acc = accuracy_score(Y_test,y_hvc_pred)
print('Accuracy:%.4f'% hvc_acc) #100% 정확도를 보임

#Bagging
#모델 학습
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=50, #트리모델 개수
                             max_depth=3, #트리의 깊이
                             random_state=20)
rfc.fit(X_train,Y_train)

#X_test의 데이터 중 처음 5개의 데이터의 예측값을 출력
y_rfc_pred = rfc.predict(X_test)
print("예측값:", y_rfc_pred[:5])

#정확도(성능)을 파악
rfc_acc = accuracy_score(Y_test,y_rfc_pred)
print('Accuracy:%.4f'% rfc_acc) #약 96.67% 정확도를 보임 (위 의사결정나무 분류처럼 1개의 트리를 사용한 것 보다 50개의 트리모델을 사용한 현 모델이 정확도가 높은 것을 알 수 있음)

#Boosting
#모델 학습
from xgboost import XGBClassifier
xgbc = XGBClassifier(n_estimators=50, max_depth=3, random_state=20)
xgbc.fit(X_train,Y_train)

#X_test의 데이터 중 처음 5개의 데이터의 예측값을 출력
y_xgbc_pred = xgbc.predict(X_test)
print("예측값:", y_xgbc_pred[:5])

#정확도(성능)을 파악
xgbc_acc = accuracy_score(Y_test,y_xgbc_pred)
print('Accuracy:%.4f'% xgbc_acc) #약 93.33% 정확도를 보임


#교차 검증

#Hold-out
#검증용 테이터셋 분리
x_tr, x_val, y_tr, y_val = train_test_split(X_train, Y_train,
                                            test_size=0.3, #30%를 검증데이터(val) , 70%를 훈련용 데이터로 분리(tr)
                                            shuffle=True,
                                            random_state=20)
print(x_tr.shape,y_tr.shape)
print(x_val.shape, y_val.shape)

#학습
rfc = RandomForestClassifier(max_depth=3, random_state=20)
rfc.fit(x_tr,y_tr)

#예측
y_tr_pred = rfc.predict(x_tr)
y_val_pred = rfc.predict(x_val)

#검증
tr_acc = accuracy_score(y_tr, y_tr_pred)
val_acc = accuracy_score(y_val, y_val_pred)
print("Train Accuracy:%.4f"%tr_acc) #약 98.8%의 정확도를 보임
print("Validation Accuracy:%.4f"%val_acc) #약 91.67%의 정확도를 보임 (Tr_acc > Val_acc 이므로 과대적합이 발생)

#테스트 데이터 예측 및 평가
y_test_pred = rfc.predict(X_test)
test_acc = accuracy_score(Y_test,y_test_pred)
print('Test Accuracy:%.4f'%test_acc) #약 90%의 정확도를 보임 (검증 정확도 보다 낮은 수준을 새로운 데이터에 대한 예측력과 성능이 낮은 편이다.)

#K-fold
#데이터셋을 5개의 Fold로 분할하는 KFold 클래스 객체 생성
from sklearn.model_selection import KFold
kfold = KFold(n_splits=5, shuffle=True, random_state=20)

#훈련용 데이터와 검증용 데이터의 행 인덱스를 각 fold 별로 구분 후 생성
num_fold = 1
for tr_idx, val_idx in kfold.split(X_train):
    print("%s Fold--------------------------------------"% num_fold)
    print("훈련:", len(tr_idx), tr_idx[:10])
    print("검증:", len(val_idx), val_idx[:10])
    num_fold = num_fold + 1

#훈련용 데이터와 검증용 데이터의 행 인덱스를 각 Fold별로 구분하여 생성
val_scores = []
num_fold = 1
for tr_idx, val_idx in kfold.split(X_train):
    #훈련용 데이터와 검증용 데이터를 행 인덱스 기준으로 추출
    x_tr, x_val = X_train.iloc[tr_idx, :], X_train.iloc[val_idx, :]
    y_tr, y_val = Y_train.iloc[tr_idx], Y_train.iloc[val_idx]

    #학습
    rfc = RandomForestClassifier(max_depth=5,random_state=20)
    rfc.fit(x_tr,y_tr)

    #검증
    y_val_pred = rfc.predict(x_val)
    val_acc = accuracy_score(y_val,y_val_pred)
    print("%d Fold Accuracy:%.4f"% (num_fold,val_acc))
    val_scores.append(val_acc)
    num_fold += 1
'''
1 Fold Accuracy:0.8750  약 87.5%
2 Fold Accuracy:1.0000  100%
3 Fold Accuracy:0.9167  약 91.67%
4 Fold Accuracy:0.9583  약 95.83%
5 Fold Accuracy:0.9565  약 95.65%
'''

mean_score = np.mean(val_scores)
print("평균 검증 Accuracy:", np.round(mean_score, 4) ) #정확도 평균값 구한후 4번째 소수점 까지 반올림 (평균 정확도: 약 94.13%)