#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from math import sqrt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.linear_model import LinearRegression
import json

def predict():
    df = pd.read_csv("final.csv" , index_col= "Date", parse_dates = True)
    a = ["New_Cases", "New_Deaths"]
    data = df[a]
    data.tail()
    data.rename(columns = {"New_Cases" : "Daily_Cases" , "New_Deaths" : "Daily_Deaths"}, inplace = True)
    data["Prev_Day_Cases"] = data["Daily_Cases"].shift(1)
    data["Prev_Day_Deaths"] = data["Daily_Deaths"].shift(1)
    data.head()
    data = data[['Daily_Cases','Prev_Day_Cases', 'Daily_Deaths','Prev_Day_Deaths']]
    data.tail()
    data.head()
    data.fillna(0, inplace = True)
    data.shape
    data.drop("Daily_Deaths", axis = 1, inplace = True)
    data.tail()
    train, test = train_test_split(data, test_size=0.2, shuffle = False)
    train.shape
    test.shape
    predictors = list(train.columns)
    predictors.remove("Daily_Cases")
    predictors
    train[predictors] # X_train
    train["Daily_Cases"] #y_train
    test[predictors] #x_test
    test["Daily_Cases"] #y_test
    lr = LinearRegression()
    lr.fit(train[predictors], train["Daily_Cases"])
    predict = lr.predict(test[predictors])
    actual = test["Daily_Cases"]
    r2_score(actual,predict)
    sqrt(mean_squared_error(predict, actual))
    final = lr.predict([[2400, 33]])
    x = { "prediction": final[0] }
    result = json.dumps(x)
    return (result)



