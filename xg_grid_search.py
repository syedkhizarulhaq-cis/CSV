# -*- coding: utf-8 -*-
"""XG_Grid Search.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UAaaBz7tqJ4U6rDOTqANGSD_mCjwEdeT
"""

import pandas as pd
import pickle
path='new_df4.csv'
Y=pd.read_csv(path, index_col='ProtocolName')

Y = Y.reset_index(drop=False)

Y.head()

y = Y['ProtocolName']
x = Y.drop(columns=['ProtocolName'])

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)
# X_train, X_test, y_train, y_test = train_test_split(x, y, stratify= y, test_size=0.20)

from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV

estimator = XGBClassifier(
    nthread=-1, 
)

parameters = {
    'n_estimators': range(1000,10000,500)
    }

grid_search = GridSearchCV(
    estimator=estimator,
    param_grid=parameters,
    scoring = 'accuracy',
    n_jobs = -1,
    cv = 4,
    verbose=True
)

# Commented out IPython magic to ensure Python compatibility.
# 
modelbest=grid_search.fit(x_train, y_train)

a=modelbest

output = open('xg1000and10000.sav', 'wb')
pickle.dump(a,output)
