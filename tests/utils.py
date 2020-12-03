import pandas as pd
from tests import data
from importlib import resources


def load_test_data(name):
    with resources.path(data, name + '.csv') as path:
        return pd.read_csv(path)