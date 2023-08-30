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

#explains distribution and transfers to data for usage
def dataBaseExplanation(filename):
    df = pd.read_csv(filename)
    df.head()
    print("CSV:",df.shape, "\n")
    data_analysis = df.describe()
    data_analysis.to_csv('output.csv', index=False)
    os.replace('output.csv', 'MLProjects\data\\data.csv')
    df.info()

#returns the rows of data
def returnDataFrame(filename):
    df = pd.read_csv(filename)
    df.head()
    return df

def dataAnalysisFDA(df):
    plt.figure(figsize=(15,8))
    plt.plot(df['Close'])
    plt.title('Tesla Closing Price', fontsize=15)
    plt.ylabel('Price in $USD')
    plt.xlabel('Days from 2010')
    plt.show()

def distributionPlotShower(df):
    print(df.head())
    df[df['Close'] == df['Adj Close']].shape
    df = df.drop(['Adj Close'], axis=1)
    print("\n")
    print('Null Checking (Any num besides 0 is undefined)\n' )
    print(df.isnull().sum())

    filters = ['Open', 'High', 'Low', 'Close', 'Volume']

    plt.subplots(figsize=(25,10))

    for i, col in enumerate(filters):
        plt.subplot(2,3,i+1)
        sb.distplot(df[col])
    plt.show()





def main():
    test_data = 'MLProjects\data\TSLA.csv'
    dataBaseExplanation(test_data)
    print("\n")
    #dataAnalysisFDA(returnDataFrame(test_data))
    distributionPlotShower(returnDataFrame(test_data))


if __name__ == "__main__":
    main()
    

