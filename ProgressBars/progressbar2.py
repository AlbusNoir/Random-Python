"""Progress bars - pandas_datareader. run in actual cmd or terminal"""
import math
import pandas_datareader as web                            # pip install pandas-datareader


def progress_bar(progress, total):
    percent = 100 * (progress / float(total))              # pass float so we don't get weird int errors
    # █ -> alt+219
    bar = '█' * int(percent) + '-' * (100 - int(percent))  # █ for completed, - for not completed
    print(f"\r|{bar}| {percent:.2f}%", end="\r")           # use return carriage, print bar over same line and show %



tickers = ["AAPL", "FB", "TSLA", "NVDA", "GS", "WFC"]
closing_prices = []

progress_bar(0, len(tickers))
for index, ticker in enumerate(tickers):
    last_price = web.DataReader(ticker, "yahoo").iloc[-1]['Close']   # grab last closing price from yahoo finance api
    closing_prices.append(last_price)
    progress_bar(index + 1, len(tickers))