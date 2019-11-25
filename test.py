import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler

data_train = pd.read_csv('train.csv')
#test_data = pd.read_csv('test.csv')

#print(data_train['SalePrice'].describe())
sns.distplot(data_train['SalePrice'])