import pandas as pd
from secStep_testConnect import TestConnect


class DataSet():
    """
    Realiza a extração dos dados
    """
    def __init__(self):
        self.teste = TestConnect().connect_web()
        self.con = self.teste
        self.table = list()
        self.teams = list()

        # First table with the name teams
        self.names_len = len(self.con.driver.find_elements_by_xpath(
            '//*[@id="classificacao__wrapper"]/article/section[1]/div/table[1]/tbody/tr'
        ))

        # Second table with the points
        self.points_len = len(self.con.driver.find_elements_by_xpath(
            '//*[@id="classificacao__wrapper"]/article/section[1]/div/table[2]/tbody/tr[1]/td'
        ))-1

        # Last games
        self.games_len = len(self.con.driver.find_elements_by_xpath(
            '//*[@id="classificacao__wrapper"]/article/section[1]/div/table[2]/tbody/tr[1]/td[10]/span'
        ))

    def scraping_data_from_website(self):

        linha = 1
        while linha <= self.names_len:
            self.teams.clear()
            nameTeam = self.con.driver.find_element_by_xpath(
                f'//*[@id="classificacao__wrapper"]/article/section[1]/div/table[1]/tbody/tr[{linha}]/td[2]/strong'
            )
            nameTeam = nameTeam.text
            self.teams.append(nameTeam)
            for i in range(self.points_len):
                pointsTeam = self.con.driver.find_element_by_xpath(
                    f'//*[@id="classificacao__wrapper"]/article/section[1]/div/table[2]/tbody/tr[{linha}]/td[{i + 1}]'
                )
                pointsTeam = pointsTeam.text
                self.teams.append(pointsTeam)

            for j in range(self.games_len):
                gamesTeam = self.con.driver.find_element_by_xpath(
                    f'//*[@id="classificacao__wrapper"]/article/section[1]/div/table[2]/tbody/tr[{linha}]/td[10]/span[{j + 1}]'
                )
                gamesTeam = str(gamesTeam.get_attribute('class').split()[1][-1])
                self.teams.append(gamesTeam)

            self.table.append(self.teams[:])
            linha += 1

        return self.table

    def data_to_dataframe(self):

        self.data = self.dataCollect()
        df = pd.DataFrame(
            self.data,
            columns=[
                'Classificação', 'P', 'J', 'v', 'E', 'D',
                'GP', 'GC', 'SG', '%', '5º últ.', '4º últ.',
                '3º últ.', '2º últ.', 'Último jogo'
            ]
        )

        return df


if __name__ == '__main__':
    web_scrap = DataSet()
    teste_connect = web_scrap.teste
    dataframe_teste = web_scrap.csv_doc()
    print(dataframe_teste)
    web_scrap.con.driver.close()
