import pandas as pd
import re


class HandlerData:
    def __init__(self, df):
        self.df = df
        self.columns = []

    def get_df(self):
        self.columns.append(self.get_column('Артикул'))
        self.columns.append(self.get_column('ИнтернетМагазин'))
        self.columns.append(self.get_column('Остаток'))
        df = self.df.iloc[:, self.columns].dropna()
        df.columns = ['_MODEL_', '_PRICE_', '_QUANTITY_']
        data_new_columns = {'_SORT_ORDER_': 110, '_STOCK_STATUS_': 'В наличии'}
        self.add_columns(df, data_new_columns)
        return df

    def get_column(self, name_data):
        s = self.df.isin([name_data]).any(axis=0)
        name_columns = s.loc[s].index.to_list()[0]
        return int(re.sub('\D', '', name_columns))

    def add_columns(self, df, data):
        for column, value in data.items():
            df[column] = value