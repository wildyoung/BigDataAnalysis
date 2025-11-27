##### STEP1. 데이터셋 불러오기
import pandas as pd
X_train = pd.read_csv('/ide/data/Pre_02_Type2_01_X_train.csv', encoding = 'cp949')
X_test = pd.read_csv('/ide/data/Pre_02_Type2_01_X_test.csv', encoding = 'cp949')
y_train = pd.read_csv('/ide/data/Pre_02_Type2_01_y_train.csv', encoding = 'cp949')

train = pd.merge(X_train, y_train, on='id')

y_train = train['stroke']
X_train = train.drop(columns=['stroke'])

X_test = X_test.copy()

# 1) 범주형 컬럼 선택
cat_cols = X_train.select_dtypes('object').columns

# 2) train + test 합치기
all_data = pd.concat([X_train, X_test], axis=0)

# 3) One-Hot 인코딩
all_data_oh = pd.get_dummies(all_data, columns=cat_cols)

# 4) 다시 분리
n_train = len(X_train)
X_train_final = all_data_oh.iloc[:n_train, :]
X_test_final = all_data_oh.iloc[n_train:, :]

#5 학습
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

model = RandomForestClassifier()
model.fit(X_train_final, y_train)
pred = model.predict(X_test_final)

result = pd.DataFrame({'pred': pred})
result.to_csv('result.csv', index=False)

