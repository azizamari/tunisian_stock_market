import pandas as pd

# manually delete PX1 and TBIDX
valos=pd.read_csv('stocks_valo.csv')
valos['Market Cap'] = valos['Market Cap'].map(lambda x: x.replace("MTND","").replace("\"",""))
valos['Market Cap'] =valos['Market Cap'].str.replace(',','.').astype(float)
valos.to_csv('stocks_valo.csv', index=False)
