#필요한 라이브러리 불러오기
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#데이터(csv) 파일 불러오기
titanic_data = './AI_Dev_code/ML_DL_Introduction/titanic_data/'                      
train = pd.read_csv(titanic_data+'train.csv')
test = pd.read_csv(titanic_data+'test.csv')
submission = pd.read_csv(titanic_data+'submission.csv')
print(train.shape, test.shape, submission.shape)

#train 데이터프레임 내용 확인
print(train.head(3))

#test 데이터프레임 내용 확인
print(test.head(2))

#submission 제출 파일 양식 확인
print(submission.head())

#train 데이터프레임 개요 정보
print(train.info())

#train 데이터프레임 통계 정보
print(train.describe(include='all'))

#결측값 분포
import missingno as msno
msno.bar(train, figsize=(10,5), color=(0.7,0.2,0.2))
plt.show()

msno.matrix(test, figsize=(10,5), color=(0.7,0.2,0.2))
plt.show()

#타이타닉 전체 데이터셋 준비
train['TrainSplit'] = 'Train'
test['TrainSplit'] = 'Test'
data = pd.concat([train, test], axis=0)
print(data.shape)

#숫자형 피처 추출
data_num = data.loc[:,['Pclass','Age','SibSp','Parch','Fare','Survived']]

#결측값 대체
data_num['Age'] = data_num['Age'].fillna(data_num['Age'].mean())
data_num['Fare'] = data_num['Fare'].fillna(data_num['Fare'].mode()[0])

#학습용 데이터와 예측 대상인 테스트 데이터 구분
selected_feature = ['Pclass','Age','SibSp','Parch','Fare']

x_train = data_num.loc[data['TrainSplit']=='Train', selected_feature]
y_train = data_num.loc[data['TrainSplit']=='Train', 'Survived']

x_test = data_num.loc[data['TrainSplit']=='Test', selected_feature]

print('Train 데이터셋 크기:', x_train.shape, y_train.shape)
print('Test 데이터셋 크기:' , x_test.shape)

#훈련 - 검증 데이터 분할
from sklearn.model_selection import train_test_split
x_tr, x_val, y_tr, y_val = train_test_split(x_train, y_train, test_size=0.2,
                                            shuffle=True, random_state=20)


#로지스틱 회귀 모델
from sklearn.linear_model import LogisticRegression
lr_model = LogisticRegression()
lr_model.fit(x_tr,y_tr)
y_val_pred = lr_model.predict(x_val)

#Confusion Matrix ------------------------
from sklearn.metrics import confusion_matrix
sns.heatmap(confusion_matrix(y_val,y_val_pred),annot=True,cbar=False,square=True)
plt.show()

#평가지표
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.metrics import f1_score, roc_auc_score
print("Accuracy:%.4f" % accuracy_score(y_val,y_val_pred))
print("Precision:%.4f" % precision_score(y_val,y_val_pred))
print("Recall:%.4f" % recall_score(y_val,y_val_pred))
print("F1 Score:%.4f" % f1_score(y_val,y_val_pred))
print("AU.C:%.4f" % roc_auc_score(y_val,y_val_pred))

#test 데이터에 대한 예측값 정리
y_test_pred = lr_model.predict(x_test)

#제출 양식에 맞게 정리
submission['Survived'] = y_test_pred.astype(int)

#제출 파일 저장
submission_filepath = titanic_data + 'baseline_num_lr_submission_001.csv'
submission.to_csv(submission_filepath, index=False)
print(submission.head(5))