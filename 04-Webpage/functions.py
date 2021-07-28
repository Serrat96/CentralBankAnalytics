import pandas as pd
import pathlib


def read_data(path: str):
        try:
                pd.read_parquet(pathlib.Path(path).absolute())
        except:
                path_2 = path[3:]
                return pd.read_parquet(pathlib.Path(path).absolute())

