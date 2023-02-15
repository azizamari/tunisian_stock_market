import requests
from io import StringIO
import pandas as pd
from all_dates import get_all_dates
from getting_data import get_data

tickers=pd.read_csv('stock_tickers.csv').ticker.values
dates=get_all_dates()
for ticker in tickers:
    print(f"handling ticker {ticker}")
    history=pd.DataFrame()
    for date in dates:
        res=get_data(ticker,date[0],date[1])
        history=pd.concat([res,history])

    history.ouverture=history.ouverture.str.replace(',','.').astype(float)
    history.haut=history.haut.str.replace(',','.').astype(float)
    history.cloture=history.cloture.str.replace(',','.').astype(float)
    history.bas=history.bas.str.replace(',','.').astype(float)
    history.date=pd.to_datetime(history.date, format="%d/%m/%Y")

    history.to_csv('data/'+ticker+'.csv',index=False)

# ouverture, haut, bas, cloture
