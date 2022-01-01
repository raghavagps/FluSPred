import re
import sys
import csv
import pandas as pd
import sys
import numpy
import pathlib
import numpy as np
import pickle
from sklearn.metrics import auc
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.cluster import KMeans
from sklearn.model_selection import GridSearchCV
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.utils import shuffle
from sklearn import metrics
from sklearn.model_selection import KFold
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import ExtraTreesClassifier

def computeML(inputDF):
    a=[]
    # file_name = sys.argv[1]
    # file_name1 = sys.argv[2]
    # file_name2 = sys.argv[3]
    clf = pickle.load(open('Models/Genome_CDK3k.sav','rb'))
    #X_test, y_test = load_svmlight_file(file_name)
    # data_test = pd.read_csv(file_name)

    data_test = inputDF


    #X_test = np.loadtxt(file_name, delimiter=',')
    X_test = data_test.drop(['Sequence_ID'], axis=1)
    #y_test = data_test[:, -1].astype(np.int)
    y_p_score1=clf.predict_proba(X_test)
    y_p_s1=y_p_score1.tolist()
    a.extend(y_p_s1)
    df = pd.DataFrame(a)
    df1 = df.iloc[:,-1].round(2)
    # df1.to_csv(file_name1, index=None, header=False)
    thr = float(0.5)
    aa = []
    for i in range(0,len(df1)):
        if df1[i] >= thr:
            aa.append("Transmissible")
        else:
            aa.append("Non-transmissible")
    df2 = pd.DataFrame(aa)


    res2 = pd.concat([data_test['Sequence_ID'], df1, df2], axis=1, sort=False)
    res2.to_csv('Output.csv',index=None, header=False)

def findModel(proteinName):
    if proteinName == "HA":
        return "Models/DPC_HA.pkl"
    elif proteinName == "M1":
        return "Models/DPC_M1.pkl"
    elif proteinName == "M2":
        return "Models/DPC_M2.pkl"
    elif proteinName == "NA":
        return "Models/DPC_NA.pkl"
    elif proteinName == "PA":
        return "Models/DPC_PA.pkl"
    elif proteinName == "PAX":
        return "Models/DPC_PAX.pkl"
    elif proteinName == "NP":
        return "Models/DPC_NP.pkl"
    elif proteinName == "NS1":
        return "Models/DPC_NS1.pkl"
    elif proteinName == "NS2":
        return "Models/AAC_NS2.pkl"
    elif proteinName == "PB1":
        return "Models/DPC_PB1.pkl"
    elif proteinName == "PB2":
        return "Models/DPC_PB2.pkl"
    elif proteinName == "PB1F2":
        return "Models/AAC_PB1F2.pkl"
    elif proteinName == "PB1N40":
        return "Models/DPC_PB1N40.pkl"
    elif proteinName == "PAN155":
        return "Models/DPC_PAN155.pkl"
    elif proteinName == "PAN182":
        return "Models/DPC_PAN182.pkl"
    else:
        return "Models/DPC_HA.pkl"
    
    


def computeMLProtein(inputDF, proteinName):
    a=[]
    
    # clf = pickle.load(open('DPC_PAX.pkl','rb'))
    clf = pickle.load(open(findModel(proteinName),'rb'))



    #X_test, y_test = load_svmlight_file(file_name)
    # data_test = pd.read_csv(file_name)

    data_test = inputDF


    #X_test = np.loadtxt(file_name, delimiter=',')
    X_test = data_test.drop(['Features'], axis=1)

    X_test = X_test.dropna(axis = 0, how ='any')



    #y_test = data_test[:, -1].astype(np.int)
    y_p_score1=clf.predict_proba(X_test)
    y_p_s1=y_p_score1.tolist()
    a.extend(y_p_s1)
    df = pd.DataFrame(a)
    df1 = df.iloc[:,-1].round(2)
    # df1.to_csv(file_name1, index=None, header=False)
    thr = float(0.5)
    aa = []
    for i in range(0,len(df1)):
        if df1[i] >= thr:
            aa.append("Transmissible")
        else:
            aa.append("Non-transmissible")
    df2 = pd.DataFrame(aa)


    res2 = pd.concat([data_test['Features'], df1, df2], axis=1, sort=False)
    res2.to_csv('Output.csv',index=None, header=False)