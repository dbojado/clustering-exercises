# ignore warnings
import warnings
warnings.filterwarnings("ignore")

# Wrangling
import pandas as pd
import numpy as np

# Exploring
import scipy.stats as stats
from scipy import stats

# Visualizing
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns

# Acquire and Prepare files
import acquire
import prepare

# Sklearn
import sklearn.preprocessing
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

df = acquire.new_mall_data()

# age, income, spending score
for col in df.describe().columns:
    q1, q2, q3 = df[col].quantile([0.25,0.5,0.75])
    IQR = q3 - q1
    
    upper = q3 + (1.5 * IQR)
    lower = q1 - (1.5 * IQR)
    
    print(upper, lower)

def split_mall_data_test(df):
    train_validate, test = train_test_split(df, test_size=.30, random_state=123)
    train, validate = train_test_split(train_validate, test_size=.20, random_state=123)
    
    # Printing the shape of each dataframe:
    print(f'Shape of train df: {train.shape}')
    print(f'Shape of validate df: {validate.shape}')
    print(f'Shape of test df: {test.shape}')
    return train, validate, test

# One Hot Encoder
ohe = OneHotEncoder(sparse=False, categories='gender')
train['is_male'] = pd.get_dummies(train.gender, drop_first = True) 
validate['is_male'] = pd.get_dummies(validate.gender, drop_first = True)
test['is_male'] = pd.get_dummies(test.gender, drop_first = True)

# Scaling Annual Income
scaler = sklearn.preprocessing.StandardScaler()
scaler.fit(train[['annual_income']])

train['annual_income_scaled'] = scaler.transform(train[['annual_income']])
test['annual_income_scaled'] = scaler.transform(test[['annual_income']])
validate['annual_income_scaled'] = scaler.transform(validate[['annual_income']])

plt.figure(figsize=(12, 5))
plt.subplot(121)
train.annual_income.plot.hist(title='Original')
plt.subplot(122)
train.annual_income_scaled.plot.hist(title='Standard Scaled')

# Scaling Spending Score 
scaler = sklearn.preprocessing.StandardScaler()
scaler.fit(train[['spending_score']])

train['spending_score_scaled'] = scaler.transform(train[['spending_score']])
test['spending_score_scaled'] = scaler.transform(test[['spending_score']])
validate['spending_score_scaled'] = scaler.transform(validate[['spending_score']])

plt.figure(figsize=(12, 5))
plt.subplot(121)
train.spending_score.plot.hist(title='Original')
plt.subplot(122)
train.spending_score_scaled.plot.hist(title='Standard Scaled')