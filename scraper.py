import requests
from bs4 import BeautifulSoup , SoupStrainer
import re


url = ["yts.am"]
types = []
quality = []
details = []

#Movie Details
class TorrentInfo:
    pass

#Main Class
class movie:
    def __init__(self , name , year):
        self.name = name
        self.year = year
    def find(self):
        for i in url:
            i = "https://"+i+"/movie/"+self.name+"-"+self.year
            webpage = requests.get(i)

            if webpage.status_code == 200:
                print("\nOpened " , i)
                print()
                
                soup1 = SoupStrainer(class_="modal-torrent")
                soup = BeautifulSoup(webpage.text , "html.parser" , parse_only = soup1)
                details = soup.find_all(class_="quality-size")
                links = []
                quality = details[1::2]
                types = details[0::2]
                for q in soup.findAll(class_="magnet-download download-torrent magnet"):
                    links.append(q.get("href"))
                return(links[0])
            else:
                print("This webpage doesn't work: " , i)

#Basic Details
film_name = list(map(str.lower , input("Enter Name of Movie: ").strip().split(' ')))
film_year = input("Enter Year of Movie: ")

film_name = '-'.join(film_name)

m1 = movie(film_name , film_year)
requests.get(m1.find())