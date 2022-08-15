from firstStep_webConnect import Connection


class TestConnect():

    def __init__(self):
        self.connect = Connection()

    def connect_web(self):

        try:
            self.connect

        except self.connect.web_exception as ERROR:
            self.connect.driver.close()
            print(f'Connection ERROR: {ERROR}')

        else:
            return self.connect
