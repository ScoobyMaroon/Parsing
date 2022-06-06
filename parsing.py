import requests
from bs4 import BeautifulSoup
dic = {'Бристоль':['https://bristol.ru/search?s=','div','product-card','product-card__title','span','price-tag__price','catalog-price','drive','red+bul','adrenaline']}

def request(url=str,first_request='',second_request='',product = '',price='',price2='',title='',spisok=list):
    listok = {}
    for i in range(len(spisok)):
        link = url + spisok[i]
        print(link)
        request = requests.get(link).text  # запрос всей страницы
        soup = BeautifulSoup(request, 'lxml')
        block = soup.find_all(first_request, product)  # достаем товар
        print(block)
        for i in range(len(block)):
            a = block[i].find(first_request, title).text
            try:
                b = block[i].find(second_request, price).text # достаем цену
            except:
                b = block[i].find(second_request, price2).text
            b = b.replace('a', 'Р')
            b = b.replace('\n', '')
            b = b.replace(' ', '')
            listok[a] = b #a
    return print(listok)
def addaptation(dic):
    a = ['Бристоль']
    for i in range(len(a)):
        b = dic[a[i]]

        url = b [0]
        first = b[1]
        product = b[2]
        title = b[3]
        second = b[4]
        price = b[5]
        price2 = b[6]
        for i in range(7):
            del b[0]
        print(b)
        print(url,first,second)
        print(b)
        request(url,first,second,product,price,price2,title,b)

addaptation(dic)
