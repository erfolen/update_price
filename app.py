import logging

from config import login_user, password, website
from login import Login
from write_read_file import ReadExel, WriteExel
from processing import Processing
from handler_data import HandlerData

# Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='info_err.log',
    filemode='a'
)

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    login = Login(login_user, password, website)
    logger.info(login.loging())
    processing = Processing(login.browser)
    processing.dowloand_file()
    login.close()
    products = ReadExel('price_mamalish.xls')
    data_products = HandlerData(products.exel_data).get_df()
    WriteExel(data_products).write_xlsx()


