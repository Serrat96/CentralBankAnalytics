import pandas as pd


def read_data(path: str):
        initial_path = r'/app/centralbankanalytics/'
        try:
                return pd.read_parquet(path)
        except:
                path_2 = path[3:]
                return pd.read_parquet(initial_path + path_2)

