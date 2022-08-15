from selenium import webdriver
from selenium.common.exceptions import WebDriverException


class Connection():

    def __init__(self):   
        self.webpage = 'https://ge.globo.com/mg/futebol/mineiro-segunda-divisao/'
        self.arquivo_chrome = r'./chromedriver.exe'
        self.web_exception = WebDriverException()
        self.driver = webdriver.Chrome(executable_path=self.arquivo_chrome)
        self.get_driver = self.driver.get(self.webpage)
