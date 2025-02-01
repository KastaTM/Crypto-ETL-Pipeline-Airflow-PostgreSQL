import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# PostgreSQL database configuration
DB_USER = "usuario"
DB_PASSWORD = "password"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "mi_basedatos"

# Conect to PostgreSQL
engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# CoinGecko API's URL
API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": False
}

def extract_data():
    response = requests.get(API_URL, params=PARAMS)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error en la API:", response.status_code)
        return None

def transform_data(data):
    df = pd.DataFrame(data)
    df = df[['id', 'symbol', 'name', 'current_price', 'market_cap', 'total_volume']]
    df.columns = ['Id', 'Symbol', 'Name', 'USD Price', 'Market Cap', 'Volume']
    df['Date'] = datetime.now()
    return df

def load_data_to_db(df):
    with engine.connect() as connection:
        df.to_sql("crypto_data", connection, if_exists="replace", index=False)
    print("Data loaded in database")


def etl_process():
    print("Initiating ETL Pipeline")
    data = extract_data()
    if data:
        df = transform_data(data)
        load_data_to_db(df)
        print("ETL Pipeline sucess.")

if __name__ == "__main__":
    etl_process()
