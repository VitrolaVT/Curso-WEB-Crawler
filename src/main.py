import requests
from bs4 import BeautifulSoup

# Site 1: https://br.ign.com/pc/
# Site 2: https://www.adrenaline.com.br/games/pc-games/

response = requests.get("https://www.adrenaline.com.br/games/pc-games/")
text = BeautifulSoup(response.text, "html.parser")
#desc1 = text.find_all("h2", {"class": "feed-title"})
desc2 = text.find("img", {"class": "attachment-444x277"})
desc3 = text.find("img", {"class": "attachment-327x204"})
#print(desc1)
print(desc2)
print(desc3)