import json
from os import getenv
import requests
import csv
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()

URL = getenv("URL")
DOMEN = getenv("DOMEN")
HEADERS ={
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
}

# response = requests.get(url=URL , headers=HEADERS)
# with open("core/html/index.html", "w") as FILE:
#     FILE.write(str(response.text))

# with open("core/html/index.html", "r") as PARSFILE:
#     page = PARSFILE.read()
# soup = BeautifulSoup(page,"lxml")
# dota = soup.find('tbody').find_all('tr')

with open("core/html/index.html", "r") as PARSFILE:
    page = PARSFILE.read()
soup = BeautifulSoup(page,"lxml")
dota_hero = soup.find('tbody').find_all('tr')

dota = {
    "Рекрут_Страж_Рыцарь": {},
    "Герой": {}
}

for item in dota_hero:
    hero = item.find('a', class_="link-type-hero").text
    (str(hero).replace('\n',"").replace('                                                   '," "))
    a = item.find_all("td")
    name =  str(a[1].text).replace('\n',"").replace('                                                   '," ")
    pick = str(a[2].text).strip()
    Win = str(a[3].text).strip()
    
    dota["Рекрут_Страж_Рыцарь"].update({
        name : f"Рейтинг героев  pick:{pick} и win:{Win}"
    })
    
for item in dota_hero:
    hero = item.find('a', class_="link-type-hero").text
    (str(hero).replace('\n',"").replace('                                                   '," "))
    a = item.find_all("td")
    name =  str(a[1].text).replace('\n',"").replace('                                                   '," ")
    pick = str(a[4].text).strip()
    Win = str(a[5].text).strip()
    
    dota["Герой"].update({
        name : f"Рейтинг героев  pick:{pick} и win:{Win}"
    })
      


    


    



# with open("core/json/dota.json", "w", encoding= "utf-8") as DOTAFILE:
#     json.dump(dota , DOTAFILE , indent= 4 , ensure_ascii= False)










































# dota_colum = soup.find('thead')
# dota_hero = soup.find('tbody').find_all('tr')
# for item in dota_hero:
#     # hero = item.find('a', class_="link-type-hero").text
#     # (str(hero).replace('\n',"").replace('                                                   '," "))
#     a = item.find_all("td")
#     name =  str(a[1].text).replace('\n',"").replace('                                                   '," ")
#     pick = str(a[2].text).strip()
#     Win = str(a[3].text).strip()
#     print(name, pick, Win)
   

# for item in dota_hero:
#     a = item.find_all("td")
#     name =  str(a[1].text).strip()
#     pick = str(a[2].text).strip()
#     Win = str(a[3].text).strip()
#     print(name, pick, Win)
    # name = item.find("a", class_="link-type-hero").text
    # recruk = item.find('td', class_="r-tab r-group-1 cell-divider cell-strong").get("data-value")

    # print(name, recruk)    
