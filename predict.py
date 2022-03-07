#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from math import sqrt, floor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.linear_model import LinearRegression
import json

def predict():
    # df = pd.read_csv("final.csv" , index_col= "Date", parse_dates = True)
    df = pd.read_csv("data_file.csv" , index_col= "Date", parse_dates = True)
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
    accuracy = r2_score(actual,predict)
    error = sqrt(mean_squared_error(predict, actual))
    previous_data_for_prediction_reference = df.tail(1).values.tolist()
    previous_day_cases_reference = previous_data_for_prediction_reference[0][1]
    previous_day_deaths_reference = previous_data_for_prediction_reference[0][3]
    
    day_before_yesterday_reference = df.tail(2).values.tolist()
    cases_this_day = day_before_yesterday_reference[1][1]
    cases_yesterday = day_before_yesterday_reference[0][1]
    percentageCases = (cases_yesterday + cases_this_day) / 2  # Take average of previous 2 days
    percentageCases = percentageCases / 10  # Take 10% of that average
    if cases_this_day > cases_yesterday:
        percentageCases = floor(abs(percentageCases + cases_this_day))  #either add or subtract that avg from today's cases
    else:
        percentageCases = floor(abs(cases_this_day - percentageCases))
    final = lr.predict([[previous_day_cases_reference, previous_day_deaths_reference]])
    cases = percentageCases
    if accuracy >= 0.83:
        cases =  final[0]
    x = { "prediction": cases, "score": r2_score(actual,predict) }
    result = json.dumps(x)
    return (result)


