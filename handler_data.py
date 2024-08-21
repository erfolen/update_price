import pandas as pd
import re


class HandlerData:
    def __init__(self, df):
        self.df = df
        self.columns = []

    def get_df(self):
        self.columns.append(self.get_columns('Артикул'))
        self.columns.append(self.get_columns('ИнтернетМагазин'))
        self.columns.append(self.get_columns('Остаток'))
        print(self.columns)
        df = self.df.iloc[:, [14, 17, 19]].dropna()
        return df

    def get_columns(self, name_data):
        s = self.df.isin([name_data]).any(axis=0)
        name_columns = s.loc[s].index.to_list()[0]
        return re.sub('\D', '', name_columns)

