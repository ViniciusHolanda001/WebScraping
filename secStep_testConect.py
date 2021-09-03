from firstStep_webConect import Conection

class TestConect():
    """
    Testa a conexão
    """
    def __init__(self):
        """
        Instancia da Classe Conection
        """
        self.conect = Conection()

    def conect_web(self):
        """
        :return: Status da conexão
        """
        try:
            self.conect
        except self.conect.web_exception as err:
            self.conect.driver.close()
            print(f'Não foi possível realizar a conexão. ERRO: {err}')
        else:
            return self.conect







