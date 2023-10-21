import requests
from bs4 import BeautifulSoup
import schedule
from datetime import datetime
import time
import json
from dotenv import load_dotenv
import os
from Database import Database
from Bot import BOT

# Site 1: https://br.ign.com/pc/
#Informações extraídas: Titulo,link e imagem
# Site 2: https://www.adrenaline.com.br/games/pc-games/
#Informações extraídas: Titulo e link

class Clawler:

    def __init__(self):
        load_dotenv()
        self.db = Database()
        self.bot = BOT()

    def request_data(self, url: str):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup

#Função para extrair do site 1
    def extract_from_IGN(self):
        raw_IGN = self.request_data("https://br.ign.com/pc/")

        #Redução das informações para pegar o que vai ser extraído

        recent_news = raw_IGN.find_all("div", {"class": "t"})

        for news in recent_news:

            #Extraindo o link, titulo e a imgagem

            link = news.find("a", {"class": "thumb score-wrapper"})
            title_image = news.find("img", {"class": "thumb"})

            data = {
                "Title": title_image.attrs["alt"],
                "Image": title_image.attrs["data-src"],
                "Link": link.attrs["href"],
                "Date": str(datetime.now())
            }

            response = self.db.insert(data)
            if response is not None:
                self.bot.post(response)

#Função para extrair do site 2
    def extract_from_ADRENALINE(self, page: int = 1):
        raw_adrenaline = self.request_data(f"https://www.adrenaline.com.br/games/pc-games/page/{page}/")

        # Redução das informações para pegar o que vai ser extraído

        recent_news = raw_adrenaline.find_all("article", {"class": "feed"})

        for news in recent_news:

            # Extraindo o link e titulo

            title = news.find("a")
            link = news.find("a")

            data = {
                "Title": title["title"],
                "Link": link.attrs["href"],
                "Date": str(datetime.now())
            }

            response = self.db.insert(data)
            if response is not None:
                self.bot.post(response)

#Função para selecionar páginas
    def execute(self, num_page: int = 3):
        for page in range(1, num_page):
            self.extract_from_ADRENALINE(page)

if __name__ == "__main__":
    crawler = Clawler()
    crawler.execute(1)

    def job():
        print("\n Execute_job Time: {}".format(str(datetime.now())))
        crawler.extract_from_IGN()
        crawler.execute()

    schedule.every(0).minutes.do(job)
    while True:
        schedule.run_pending()