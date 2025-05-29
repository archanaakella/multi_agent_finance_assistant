import sqlite3
import pandas as pd

DB_FILE = "market_data.db"

def create_db():
    """Initialize the SQLite database and table."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS stock_data (
        symbol TEXT,
        date TEXT,
        open REAL,
        high REAL,
        low REAL,
        close REAL,
        volume INTEGER
    )
    """)
    conn.commit()
    conn.close()

def cache_market_data(symbol, data):
    """Store market data into SQLite database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    for index, row in data.iterrows():
        cursor.execute("INSERT INTO stock_data VALUES (?, ?, ?, ?, ?, ?, ?)", 
                       (symbol, index, row['1. open'], row['2. high'], row['3. low'], row['4. close'], row['5. volume']))
    
    conn.commit()
    conn.close()

def retrieve_cached_data(symbol):
    """Fetch cached market data from SQLite."""
    conn = sqlite3.connect(DB_FILE)
    query = f"SELECT * FROM stock_data WHERE symbol='{symbol}'"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

if __name__ == "__main__":
    create_db()
    symbol = "AAPL"
    cached_df = retrieve_cached_data(symbol)
    print(cached_df.head())