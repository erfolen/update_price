import copy
import pandas as pd
import math
import re


class ReadExel:
    """
    Получение из файла данных о товаре
    """

    def __init__(self, name_file):
        self.exel_data = pd.read_excel(name_file)


class WriteExel:
    """Запись заказа в файл"""

    def __init__(self, df):
        self.df = df

    def write_xlsx(self):
        self.df.to_csv('price_mamalish.csv', sep=';', index=False)
