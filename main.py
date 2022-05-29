import requests
from bs4 import BeautifulSoup
links = ['https://www.bristol.ru/catalog/?how=r&q=drive','https://www.bristol.ru/catalog/?how=r&q=red+bul'] # сайт
spisok = {}
for i in range(len(links)):
    link = links[i]
    request = requests.get(link).text # запрос всей страницы
    soup = BeautifulSoup(request,'lxml')
    block = soup.find_all('div', 'contentListItem') #достаем товар
    for i in range(len(block)):
        a = block[i].find('div', 'catalog-title').text
        try:b = block[i].find('span', 'catalog-price new').text
        except: b = block[i].find('span', 'catalog-price').text
        b = b.replace('a', 'Р')
        b = b.replace('\n','')
        b = b.replace(' ','')
        spisok[a] = b
print(spisok)