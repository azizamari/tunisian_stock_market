import requests
from io import StringIO
import pandas as pd
from all_dates import get_all_dates
from getting_data import get_data

tickers=pd.read_csv('stock_names.csv').name.values
dates=get_all_dates()
for ticker in tickers[:1]:
    print(f"handling ticker {ticker}")
    history=pd.DataFrame()
    for date in dates:
        res=get_data(ticker,date[0],date[1])
        history=pd.concat([res,history])
    history.to_csv(ticker+'.csv',index=False)
