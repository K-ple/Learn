#판다스 라이브러리 삽입
import pandas as pd
print(pd.__version__)

#데이터 인덱스 나열
data1 = ['a','b','c','d','e']
print(data1)
print("자료형:", type(data1))

#Series 객체 변환
sr1 = pd.Series(data1)
print("자료형:", type(sr1))

print(sr1)

#해당 위치 인덱스 값 출력
print(sr1.loc[0])

#범위 내 인덱스와 값 출력
print(sr1.loc[1:3])

#튜플형 플롯 데이터 벡터 나열
data2 = (1,2,3.14,100,-10)
sr2 = pd.Series(data2)
print(sr2)

#딕셔너리 형 데이터 결합
dict_data = {'c0':sr1, 'c1':sr2}
df1 = pd.DataFrame(dict_data)
print(df1)

print(type(df1))

print(df1.columns)

#딕셔너리 열배열 제목 변경
df1.columns = ['string','number']
print(df1)

#인덱스 시작과끝 차순 추출
print(df1.index)

#행인덱스
df1.index = ['r0','r1','r2','r3','r4']
print(df1)

#지정된 행인덱스와 열인덱스가 일치하는 값을 출력
print(df1.loc['r2','number'])

#지정된 행인덱스 범위와 열인덱스범위에 해당되는 값을 모두 출력
print(df1.loc['r2':'r3','string':'number'])

#지정된 행인덱스 범위와 1개의 열인덱스에 해당되는 값을 모두 출력
print(df1.loc['r2':'r3','number'])

#지정된 행인덱스에 해당되는 열인덱스 범위값을 모두 출력
print(df1.loc['r2','string':'number'])

#모든 행인덱스 중 지정된 열인덱스에 해당되는 값을 모두 출력
print(df1.loc[:,'string'])

#지정된 행인덱스 범위에 해당되는 모든 열인덱스 출력
print(df1.loc['r2':'r3', :])