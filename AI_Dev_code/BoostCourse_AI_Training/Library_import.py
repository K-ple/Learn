# Suppress warnings
import warnings
warnings.filterwarnings('ignore')

import os, sys, gc, warnings, random

import datetime
import dateutil.relativedelta

# Data manipulation
import pandas as pd
import numpy as np

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Machine Learning
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, precision_recall_curve, roc_curve
from sklearn.model_selection import train_test_split, cross_val_score, KFold, StratifiedKFold, GroupKFold
from sklearn.ensemble import RandomForestClassifier

import lightgbm as lgb

from tqdm.notebook import trange, tqdm

from IPython.display import display

#matplotlib inline

pd.options.display.max_rows = 10000
pd.options.display.max_columns = 1000
pd.options.display.max_colwidth = 1000


TOTAL_THRES = 300
'''
    입력인자로 받는 year_month에 대해 고객 ID별로 총 구매액이
    구매액 임계값을 넘는지 여부의 binary label을 생성하는 함수
'''
def generate_label (df, year_month, total_thres=TOTAL_THRES, print_log=False):
    df = df.copy()

    # year_month에 해당하는 label 데이터 생성
    df['year_month'] = df['order_date'].dt.strftime('%Y-%m')
    df.reset_index(drop=True, inplace=True)

    #year_month 이전 월의 고객 ID 추출
    cust = df[df['year_month'] < year_month]['customer_id'].unique()
    #year_month에 해당하는 데이터 선택
    df = df[df['year_month'] == year_month]

    # label 데이터프레임 생성
    label = pd.DataFrame({'customer_id': cust})
    label['year_month'] = year_month

    #year_month에 해당하는 고객 ID의 구매액의 합 계산
    grped = df.groupby(['customer_id', 'year_month'], as_index=False)[['total']].sum()

    # label 데이터프레임과 merge하고 구매액 임계값을 넘었는지 여부로 label 생성
    label = label.merge(grped, on=['customer_id', 'year_month'], how='left')
    label['total'].fillna(0.0, inplace=True)
    label['label'] = (label['total'] > total_thres).astype(int)

    # 고객 ID로 정렬
    label = label.sort_values('customer_id').reset_index(drop=True)
    if print_log: print(f'{year_month} - final label shape: {label.shape}')

    return label

#평가지표 출력 함수 정의
def print_score(label, pred, prob_thres=0.5):
    print('Precision: {:.5f}'.format(precision_score(label, pred>prob_thres)))
    print('Recall: {:.5f}'.format(recall_score(label, pred>prob_thres)))
    print('F1-score: {:.5f}'.format(f1_score(label, pred>prob_thres)))
    print('ROC AUC Score: {:.5f}'.format(roc_auc_score(label, pred)))

#Train 데이터 읽기
data = pd.read_csv('./data/train.csv', parse_dates=['order_data'])
print(data.shape)
data.head()

#Pandas info() 함수로 데이터 타입 및 null 체크
print(data.info())

#Pandas isna(), sum() 함수로 null 데이터 개수 체크
print(data.isna().sum())

#null 데이터 비율 체크
print(data.isna().sum()/data.shape[0])

#Pandas describe() 함수로 수치형 데이터 기본 통계량 확인
print(data.describe())

#Pandas describe() 함수에 include='all' 인자 설정으로 수치형, 범주형 데이터 기본 통계량 확인
print(data.describe(include='all'))

#베이스라인 모델 함수
'''
    머신러닝 모델 없이 입력인자로 받는 year_month의 이전 달 총 구매액을 구매 확률로 예측하는 베이스라인 모델
'''
def baseline_no_ml(df, year_month, total_thres=TOTAL_THRES):
    # year_month에 해당하는 label 데이터 생성
    month = generate_label(df, year_month)

    # year_month 이전 월 계산
    d = datetime.datetime.strptime(year_month, '%Y-%m')
    prev_d = d - dateutil.relativedelta.relativedelta(months=1)
    prev_d = prev_d.strftime('%Y-%m')

    #이전 월에 해당하는 label 데이터 생성
    previous_month = generate_label(df, prev_d)

    #merge하기 위해 컬럼명 변경
    previous_month = previous_month.rename(columns= {'total' : 'previous_total'})

    month = month.merge(previous_month[['customer_id', 'previous_total']], on='customer_id', how= 'left')

    #거래내역이 없는 고객의 구매액을 0으로 채움
    month['previous_total'] = month['previous_total'].fillna(0)
    #이전 월의 총 구매액을 구매액 임계값으로 나눠서 예측 확률로 계산
    month['probability'] = month['previous_total'] / total_thres

    #이전 월 총 구매액이 구매액 임계값을 넘어서 1보다 클 경우 예측 확률을 1로 변경
    month.loc[month['probability'] > 1, 'probability'] = 1

    #이전 월 총 구매액이 마이너스(주문 환불)일 경우 예측 확률을 0으로 변경
    month.loc[month['probability'] < 0, 'probability'] = 0

    return month['probability']

#2011년 11월 Label 데이터 생성
label_2011_11 = generate_label(data, '2011-11')['label']

#Label 데이터 분포 플롯
sns.countplot(label_2011_11)
label_2011_11.value_counts()

#2011년 11월 베이스라인 모델 예측
test_preds_2011_11 = baseline_no_ml(data, '2011-11')
print_score(label_2011_11, test_preds_2011_11)

#2011년 11월 베이스라인 모델 예측 데이터 분포
sns.distplot(test_preds_2011_11)
plt.show()

#2011년 12월 베이스라인 모델 예측
test_preds = baseline_no_ml(data, '2011-12')

#2011년 12월 베이스라인 모델 예측 데이터 분포
sns.distplot(test_preds)
plt.show()

