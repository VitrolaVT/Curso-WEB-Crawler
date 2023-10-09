import requests
from bs4 import BeautifulSoup

# Site 1: https://br.ign.com/pc/
#Informações extraídas: Titulo,link e imagem
# Site 2: https://www.adrenaline.com.br/games/pc-games/
#Informações extraídas: Titulo e link

class Clawler:
    def request_data(self, url: str):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup

#Função para extrair do site 1
    def extract_from_IGN(self):
        raw_IGN = self.request_data("https://br.ign.com/pc/")

        #Redução das informações para pegar o que vai ser extraído

        recent_news = raw_IGN.find_all("div", {"class": "t"})

        all_data = []
        for news in recent_news:

            #Extraindo o link, titulo e a imgagem

            link = news.find("a", {"class": "thumb score-wrapper"})
            title_image = news.find("img", {"class": "thumb"})

            data = {
                "Title": title_image.attrs["alt"],
                "Image": title_image.attrs["data-src"],
                "link": link.attrs["href"]
            }
            all_data.append(data)

            print(data)

#Função para extrair do site 2
    def extract_from_ADRENALINE(self):
        raw_adrenaline = self.request_data("https://www.adrenaline.com.br/games/pc-games/")

        # Redução das informações para pegar o que vai ser extraído

        recent_news = raw_adrenaline.find_all("article", {"class": "feed"})

        all_data = []
        for news in recent_news:

            # Extraindo o link e titulo

            title = news.find("a")
            link = news.find("a")

            data = {
                "Title": title["title"],
                "link": link.attrs["href"]
            }
            all_data.append(data)

            print(data)
if __name__ == "__main__":
    crawler = Clawler()
    crawler.extract_from_IGN()
    crawler.extract_from_ADRENALINE()
