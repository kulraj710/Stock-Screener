import pandas_datareader as web
import pandas as pd
from yahoo_fin import stock_info as si
import datetime as dt

# tickers = si.tickers_nifty50()
tickers = si.tickers_sp500()

start = dt.datetime.now() - dt.datetime(days=365)
end = dt.datetime.now()

nifty50_df = web.DataReader('^GSPC', 'yahoo', start, end)

nifty50_df['Pct Change'] = nifty50_df['Adj Close'].pct_change()

nifty50_return = (nifty50_df['Pct Change'] + 1).cumprod()[-1]


return_list = []
final_df = pd.DataFrame(columns=['Ticker', 'Latest_Price', 'Score', 'PE_Ratio', 'PEG_Ratio', 'SMA_150', 'SMA_200', '52_Week_Low', '52_Week_High'])

for ticker in tickers:
    df = web.DataReader(ticker, 'yahoo', start, end)
    df.to_csv(f'stock_data/{ticker}.csv')
    
    df['Pct Change'] = df['Adj Close'].pct_change()
    
    stock_return = (df['Pct Change'] + 1).cumprod()[-1]
    
    returns_compared = round((stock_return / nifty50_return), 2)
    
    return_list.append(returns_compared)


