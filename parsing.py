from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
link = ['https://myspar.ru/catalog/energetiki-kofeynye-napitki/f/brand-is-']
shop = ['SPAR','Окей']
links = {'SPAR' : ['https://myspar.ru/catalog/energetiki-kofeynye-napitki/f/brand-is-','catalog-tile'],
         'Окей':['https://www.okeydostavka.ru/webapp/wcs/stores/servlet/SearchDisplay?categoryId=&storeId=10151&catalogId=12051&langId=-20&sType=SimpleSearch&resultCatEntryType=2&showResultsPage=true&searchSource=Q&pageView=&beginIndex=0&pageSize=72&searchTerm=',
                 'product']}
product = ['adrenaline','black-monster'] #'adrenaline','black-monster','burn','drive-me','gorilla','red-bull','tornado'
def spar(b=list):
    for i in range(2):
        del b[0]
    del b[-1]
    if b[-2] == 'ж/б' or b[-2] == 'Ж/Б':
        del b[-2]
    price = b[-1]
    price = price.replace('руб.', '')
    price = int(price) / 100
    price = format(price, '.2f')
    v = b[-2]
    v = v.replace('л', '')
    v = float(v.replace(',', '.'))
    for i in range(2):
        del b[-1]
    name = ''
    for i in b:
        name += f'{i} '
    name = name
    return name,v,price
def okey(b=list):
    for i in range(2):
        del b[0]
        del b[-1]
    del b[-1]
    del b[-2]
    price = b[-1]

    v = b[-2]
    v = v.replace(',','.')
    try:
        v = float(v)
    except:
        v= 0.0
    del b[-1]
    del b[-1]
    name = ''
    for i in b:
        if i == '...':
            continue
        else:
            name +=f'{i} '
    print(price,v,name)
    return name, v, price
class Energy:
    def __init__(self,b=list,shop=''):
        if shop == 'SPAR':
            b = spar(b)
        if shop == 'Окей':
            b = okey(b)
        self.name = b[0]
        self.v = b[1]
        self.price = b[2]
    def __str__(self):
        return f'{self.name} ОБЪЕМ {self.v}л ПО ЦЕНЕ {self.price}Р'

def connection(link):
    driver = webdriver.Chrome()
    driver.get(link)
    driver.fullscreen_window()
    return driver

def get_products(driver,tag,shop):
    d = []
    a = driver.find_elements_by_class_name(tag)
    for i in a:
        print(i.text.split())
        d.append(Energy(i.text.split(),shop))
    return d

def create_url(link1,product,tag,shop):

    url = link1 + product
    d = (get_products(connection(url),tag,shop))
    return d
def mess(itog):
    mess = ''
    for i in itog:
        for g in i:
           sticker = ''
           if g.name[:10] == 'Adrenaline':
               sticker = '🍸'
           if g.name[:5] == 'Black':
               sticker = '😈'
           if g.name[:4] == 'Burn':
               sticker='🌴'
           if g.name[:5] == 'Drive':
               sticker='⚡'
           if g.name[:7] == 'Gorilla':
               sticker='🦍'
           if g.name[:8] == 'Red Bull':
               sticker='🐅'
           if g.name[:7] == 'Торнадо':
               sticker='🌪'
           mess +=f'{sticker}{g}\n\n'
    return mess
def start(shop,product):
    itog = []
    for i in product:
        d = create_url(links[shop][0], i,links[shop][1],shop)
        itog.append(d)
    itog = mess(itog)
    return itog
