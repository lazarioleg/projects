
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn import metrics

import warnings
warnings.filterwarnings("ignore")


def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


def logistic_training(df):
    # Split the data into features (X) and target variable (y)
    X = df.drop('target', axis=1)
    y = df['target']


    X_train, X_valid, Y_train, Y_valid = train_test_split(X, y, test_size=0.2, random_state=42)

   
    models = [
        ('Logistic Regression', LogisticRegression()),
        ('SVM (Poly Kernel)', SVC(kernel='poly', probability=True)),
        ('XGBoost', XGBClassifier())
    ]

    
    for model_name, model in models:
        model.fit(X_train, Y_train)

        
        train_auc = metrics.roc_auc_score(Y_train, model.predict_proba(X_train)[:, 1])
        valid_auc = metrics.roc_auc_score(Y_valid, model.predict_proba(X_valid)[:, 1])

        
        print(f'{model_name} :')
        print('Training Accuracy : ', train_auc)
        print('Validation Accuracy : ', valid_auc)
        print()



if __name__ == "__main__":
    data_path = 'MLProjects\data\TSLA.csv'
    stock_data = load_data(data_path)

    logistic_training(stock_data)

