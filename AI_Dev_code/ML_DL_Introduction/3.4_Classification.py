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
df.columns = ['sepal length', 'sepal width', 'petal length', 'petal width']
print(df.head(2)) #2번째 데이터까지만 출력

#데이터 프레임 열 추가 (가장 오른쪽 열)
df['Target'] = iris['target'] # Target 이름의 열을 생성 및 나열 (class: 0, 1, 2)
print('데이터셋의 크기:', df.shape)
print(df.head())
