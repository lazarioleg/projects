import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import logisticregression
 
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
    splitted = df['Date'].str.split('/', expand=True)
    splitted = df['Date'].str.split('/', expand=True)
    
    df['day'] = splitted[1].astype('int')
    df['month'] = splitted[0].astype('int')
    df['year'] = splitted[2].astype('int')

    #quarter checking
    df['is_quarter_end'] = np.where(df['month']%3==0,1,0)
    
    df.head()
    return df;

def dataAnalysisFDA(df):
    plt.figure(figsize=(15,8))
    plt.plot(df['Close'])
    plt.title('Tesla Closing Price', fontsize=15)
    plt.ylabel('Price in $USD')
    plt.xlabel('Days from 2010')
    plt.show()

features = ['Open', 'High', 'Low', 'Close', 'Volume']

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

    #left-skewed data fix soon

    plt.subplots(figsize=(20,10))
    for i, col in enumerate(features):
        plt.subplot(2,3,i+1)
        sb.boxplot(df[col])
    plt.show()


def barGraphShower(df):
    #fix errors in terminal
    
    data_grouped = df.groupby('year').mean()
    plt.subplots(figsize=(20,10))
    
    for i, col in enumerate(['Open', 'High', 'Low', 'Close']):
        plt.subplot(2,2,i+1)
        data_grouped[col].plot.bar()
    plt.show()


def pieGraphShower(df):
    plt.pie(df['target'].value_counts().values,
        labels=[0, 1], autopct='%1.1f%%')
    plt.show()


def heatMapMaker(df):
    plt.figure(figsize=(10, 10))
    sb.heatmap(df.corr() > 0.9, annot=True, cbar=False)
    plt.show()
    features = df[['open-close', 'low-high', 'is_quarter_end']]
    target = df['target']
    
    scaler = StandardScaler()
    features = scaler.fit_transform(features)
    
    X_train, X_valid, Y_train, Y_valid = train_test_split(
        features, target, test_size=0.1, random_state=2022)
    print(X_train.shape, X_valid.shape)


def confusionMatrix(df, model, X_valid, Y_valid):
    metrics.plot_confusion_matrix(model, X_valid, Y_valid)
    plt.show()



def main():
    test_data = 'MLProjects\data\TSLA.csv'
    dataBaseExplanation(test_data)
    print("\n")
    #dataAnalysisFDA(returnDataFrame(test_data))
    distributionPlotShower(returnDataFrame(test_data))
    barGraphShower(returnDataFrame(test_data))


if __name__ == "__main__":
    main()
    

