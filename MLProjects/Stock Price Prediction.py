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

def dataBaseExplanation(filename):
    df = pd.read_csv(filename)
    df.head()
    print("CSV:",df.shape, "\n")
    data_analysis = df.describe()
    data_analysis.to_csv('output.csv', index=False)
    os.replace('output.csv', 'MLProjects\data\\data.csv')


def main():
    dataBaseExplanation('MLProjects\data\TSLA.csv')

if __name__ == "__main__":
    main()
    

