from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    """Вход на сайт"""
    def __init__(self, login, password, website):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(20)
        self.login = login
        self.password = password
        self.website = website
        self.is_loging = False

    def get_site(self):
        self.browser.get(self.website)
        self.browser.maximize_window()

    def loging(self):
        try:
            self.get_site()
            user_input = self.browser.find_element('name','USER_LOGIN')
            user_input.clear()
            user_input.send_keys(self.login)
            pasw_input = self.browser.find_element('name','USER_PASSWORD')
            pasw_input.clear()
            pasw_input.send_keys(self.password)
            self.browser.find_element('name','Login').click()
            self.is_loging = True
            return 'Осуществлен вход на сайт'
        except:
            self.is_loging = False
            return 'Не работает сайт'

    def get_browser(self):
        return self.browser

    def close(self):
        self.browser.close()
        self.browser.quit()

