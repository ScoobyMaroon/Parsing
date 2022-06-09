from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
link = ['https://myspar.ru/catalog/energetiki-kofeynye-napitki/f/brand-is-']
shop = ['SPAR']
product = ['adrenaline','black-monster','burn','drive-me','gorilla','red-bull','tornado'] #'adrenaline','black-monster','burn','drive-me','gorilla','red-bull','tornado'
class Energy:

    def __init__(self,b=list):
        for i in range(2):
            del b[0]
        del b[-1]
        if b[-2] == 'ж/б' or b[-2] == 'Ж/Б':
            del b[-2]
        price = b[-1]
        price = price.replace('руб.', '')
        price = int(price) / 100
        self.price = format(price, '.2f')
        v = b[-2]
        v = v.replace('л', '')
        self.v = float(v.replace(',', '.'))
        for i in range(2):
            del b[-1]
        name = ''
        for i in b:
            name += f'{i} '
        self.name = name
    def __str__(self):
        return f'{self.name} {self.price}'

def connection(link):
    driver = webdriver.Chrome()
    driver.get(link)
    driver.fullscreen_window()
    return driver
def get_products(driver):
    d = []
    a = driver.find_elements_by_class_name('catalog-tile')
    for i in a:
        print(i.text.split())
        d.append(Energy(i.text.split()))
    return d
def create_url(link1,product):

    url = link1 + product
    d = (get_products(connection(url)))
    return d


