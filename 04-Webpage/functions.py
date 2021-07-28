import pandas as pd
import pathlib


def read_data(path: str):
        return pd.read_parquet(pathlib.Path(path).absolute())

