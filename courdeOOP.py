import requests
import random
from bs4 import BeautifulSoup
from config import HOST, URL_EURO, URL_BUCKS, HEADERS, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK
import re


class Course():

    def __init__(self, HOST, URL_BUCKS, URL_EURO, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK):
        self.HOST = HOST
        self.URL_BUCKS = URL_BUCKS
        self.URL_EURO = URL_EURO
        self.URL_PORN = URL_PORN
        self.URL_WEATHER = URL_WEATHER
        self.URL_EDA = URL_EDA
        self.URL_ANEKDOT = URL_ANEKDOT
        self.URL_GOROSKOP = URL_GOROSKOP
        self.URL_PRAZDNIK = URL_PRAZDNIK

    def get_HTML(self, url, params=''):
        self.URL_PORN = self.URL_PORN + str(random.randint(1, 2273))
        r = requests.get(url, headers=HEADERS, params=params)
        return r


    def get_WEATHER(self, html):
        soup = BeautifulSoup(html.text, 'html.parser')
        items = soup.find('div', class_='temp').get_text()
        veter = soup.find('div', class_='details').get_text()
        return items, veter
    

    def get_CONTENT(self, html):
        soup = BeautifulSoup(html.text, 'html.parser')
        items = soup.find_all('div', class_='currency-table')
        currency = []
        
        for item in items:
            currency.append(
                item.find('div', class_='currency-table__large-text').get_text()   
            )
        return (str(currency[0].replace(',', '.')))

    def get_ANEKDOT(self, html):
        soup = BeautifulSoup(html.text, 'html.parser')
        items = soup.find('div', class_='text').get_text() 
        return(items)

    
    def get_EDA(self, html):
        soup = BeautifulSoup(html.text, 'html.parser')
        items = soup.find('a', class_='btnGreen2 flR')
        recept = soup.find('div', class_='navigation')
        izobr = soup.find('img', class_='img2')
        eda = []
        
        for i in soup.find_all('a', class_='btnGreen2 flR'):
            eda.append(i.get('href'))
            
        return 'https:'+str(eda[0])
        

    def get_EDA_photo(self, html):
        soup = BeautifulSoup(html.text, 'html.parser')
        izobr = soup.find('img', class_='img2')
        hui = []
        for i in soup.find_all('img', class_='img2'):
            hui.append(i.get('src'))
        
        return 'https:'+str(hui[0])


    def get_porn_CONTENT(self, html):
        soup = BeautifulSoup(html.text, 'html.parser')
        rand_porn = []
        rand_porn2 = []
            
        for i in soup.find_all('a', class_=''):
            rand_porn.append(i.get('href'))

        strings = 'view_video.php'
        for i in rand_porn:
            match = re.search(strings, i)
            if match:
                rand_porn2.append(i)
            else:
                continue
        return ('https://rt.pornhub.com'+ str(random.choice(rand_porn2)))

    
    def get_goroskop(self, html):
        soup = BeautifulSoup(html.text, 'html.parser')
        items = soup.find('article', class_='oculus-epz-text').get_text()
        return items


    def get_prazdnik(self, html):
        soup = BeautifulSoup(html.text, 'html.parser')
        items = soup.find('div', class_='prazdnik').get_text()
        return items
        


COURSE = Course(HOST, URL_BUCKS, URL_EURO, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK)
html = COURSE.get_HTML(URL_WEATHER)
(str(COURSE.get_WEATHER(html)).replace('(', '')).replace(')', ''))

string = "(4324243242)"






