import pandas as pd


def read_data(path: str):
    try:
        return pd.read_parquet(path)
    except:
        initial_path = r'/app/centralbankanalytics/'
        path_2 = path[3:]
        return pd.read_parquet(initial_path + path_2)
