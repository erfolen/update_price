from selenium.webdriver.common.by import By
import requests

class Processing:
    """Обработка сайта"""
    def __init__(self, browser):
        self.browser = browser


    def dowloand_file(self):
        """Скачивает прайс"""
        element = self.browser.find_element(By.ID, 'bx_3218110189_75398')
        file_url = element.find_element(By.TAG_NAME, 'a').get_attribute('href')
        response = requests.get(file_url)

        # Сохраняем файл
        with open('price_mamalish.xls', 'wb') as file:
            file.write(response.content)
