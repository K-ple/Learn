#필요한 라이브러리 불러오기
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#데이터(csv) 파일 불러오기
tt_path = "./4.1_titanic_data/"
train = pd.read_csv(tt_path+'train.csv')
test = pd.read_csv(tt_path+'test.csv')
submission = pd.read_csv(tt_path+'submission.csv')

print(train.shape, test.shape, submission.shape)