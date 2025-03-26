import pandas as pd
import plotly.express as px
import statsmodels.api as sm
from statsmodels.tsa import stattools
import numpy as np

def line_plot(data):
    '''
    This function plot a line chart
    '''
    fig = px.line(data, x = data.columns[0], y = data.columns[1])

    fig.update_layout(xaxis_title = data.columns[0],
                      yaxis_title = data.columns[1],
                      title = {'text': data.columns[1], 'x': 0.5, 'xanchor': 'center'})
    
    fig.show()

def is_stationary(series):
    '''
    This function check if a time series is stationary or not.
    The return value is boolean: True if the time series is stationary, and False if the time series is non stationary
    '''
    regression = 'c'
    result = stattools.adfuller(series, regression=regression)
    # The 2nd value returned from adfuller() is the p-value. If the p-value > 0.05 then the null hypothesis is true (stationary)
    #return result[1] <= 0.05
    return result

def transform_stationary(series, method, period):
    '''
    This function transform the time series in order to make it stationary
    '''
    if method == 'diff':
        new = series.diff(periods = period)
        return new
    elif method == 'rolling':
        return series - series.rolling(window = period).mean()
    elif method == 'log':
        new = np.log(series)
        return new
    elif method == 'decompose':
        result = sm.tsa.seasonal_decompose(series, model='additive', period=4)
        return result.resid