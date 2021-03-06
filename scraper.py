import requests
from bs4 import BeautifulSoup , SoupStrainer
import re
import sys , subprocess

url = ["yts.am" , "yts.unblocked.llc" , "yts.pm"]
types = []
quality = []
details = []


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
                quality = [x.contents[0] for x in quality]
                types = [x.contents[0] for x in types]
                
                k = 0

                #Uncomment to also get corresponding links
                # for k,x,y,z in zip(range(len(links)) , types,quality , links): 
                #     print(k , " " , x , " " , y , "\n\n" , z , "\n\n") 
                # this_link = int(input("Which Link? Indexwise: "))
                
                #Comment this and uncommment above if you want the links
                for k,x,y in zip(range(len(links)) , types , quality): 
                    print(k , " " , x , " " , y , "\n\n") 
                this_link = int(input("Which Link? Indexwise: "))
                

                subprocess.Popen(['xdg-open', links[this_link]],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                break
            else:
                print("This webpage doesn't exist: " , i)

#Basic Details
film_name = list(map(str.lower , input("Enter Name of Movie: ").strip().split(' ')))
film_year = input("Enter Year of Movie: ")

film_name = '-'.join(film_name)

m1 = movie(film_name , film_year)
m1.find()