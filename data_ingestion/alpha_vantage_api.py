from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import time

# AlphaVantage API Key
API_KEY = "ZJ64PL2I3MSZ3WT3"

# Initialize AlphaVantage API Client
ts = TimeSeries(key=API_KEY, output_format="pandas")

def get_intraday_data(symbol, interval="5min"):
    """Fetch intraday market data for a given stock symbol."""
    try:
        data, meta_data = ts.get_intraday(symbol=symbol, interval=interval, outputsize="full")
        return data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def get_daily_data(symbol):
    """Fetch daily historical market data."""
    try:
        data, meta_data = ts.get_daily(symbol=symbol, outputsize="full")
        return data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

# Example Usage
if __name__ == "__main__":
    stock_symbol = "AAPL"
    df = get_intraday_data(stock_symbol)
    if df is not None:
        print(df.head())