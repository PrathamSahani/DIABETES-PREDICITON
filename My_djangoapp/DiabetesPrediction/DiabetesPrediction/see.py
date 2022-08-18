from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score



def home(request):
    return render(request, 'home.html')
def see(request):
    return render(request, 'see.html')
def result(request):
    heart_data = pd.read_csv(r"C:\Users\rsp.tech Solution\OneDrive\Desktop\My_djangoapp\DiabetesPrediction\heart.csv")
    X = heart_data.drop(columns='target', axis=1)
    Y= heart_data['target']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)
   
    classifier = LogisticRegression()
    classifier.fit(X_train, Y_train)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])
    val9 = float(request.GET['n9'])
    val10 = float(request.GET['n10'])
    val11 = float(request.GET['n11'])
    val12 = float(request.GET['n12'])
    val13 = float(request.GET['n13'])

    pred =  classifier.predict([[val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, val11, val12, val13]])

    result1= ""
    if pred==[1]:
        result1="Oops! You have Heart Diasease 😔."
    else:
        result1="Great! You DON'T have Heart Diasease  😁."

        
    return render(request, "see.html", {"result2":result1})

