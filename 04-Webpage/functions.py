import pandas as pd


def read_data(path: str):
    try:
        return pd.read_parquet(path)
    except:
        return pd.read_parquet('.' + path)
