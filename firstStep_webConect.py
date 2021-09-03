from selenium import webdriver
from selenium.common.exceptions import WebDriverException

class Conection():
    """
    Uma classe para inicializar o webdriver do selenium
    """
    def __init__(self):
        """
        Inicializa o webdriver
        """
        # Identifica a página
        self.webpage = 'https://ge.globo.com/mg/futebol/mineiro-segunda-divisao/'

        # Arquivo chromedriver
        self.arquivo_chrome = r'./chromedriver.exe'

        # Selenium exception
        self.web_exception = WebDriverException()

        # Inicializa webdriver
        self.driver = webdriver.Chrome(executable_path=self.arquivo_chrome)
        self.get_driver = self.driver.get(self.webpage)


