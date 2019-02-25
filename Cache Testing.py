#region
#ax = pickle.load(open('bollingerbands.pickle', 'rb'))
#endregion
import pandas as pd
from typing import Dict
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import numpy as np
import pickle
import quandl
from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='MCD3GDSY1WYI9LA1', output_format='pandas')
data, meta = ts.get_daily_adjusted(symbol='BOOM', outputsize='full')
print(data.columns)

