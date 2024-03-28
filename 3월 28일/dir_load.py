import os
from glob
import pandas as pd

def read_df(_path, _encoding='utf-8'):
    head, tail = os.path.splitext(_path)
    if tail == '.csv':
        df = pd.read_csv(_path, encoding=_encoding)
    elif tail == '.json':
        df = pd.read_json(_path, encoding=_encoding)
    elif tail == '.xml':
        df = pd.read_xml(_path, encoding=_encoding)
    elif tail in ['.xlsx', '.xls']:
        df = pd.read_excel(_path)
    else:
        df = pd.DataFrame()
    return df