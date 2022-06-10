import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
vk_session = vk_api.VkApi(token='dfc4a16561b301baf13a27364bff58168642b179ffd762f56221aa1de97960a7ade5833c3aff0513a4786')
from vk_api.longpoll import VkLongPoll, VkEventType
from parsing import shop,create_url,link,start
from vk_api import utils
import time
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

def send_message(user_id,message,keyboard=None):
    post = {
        "user_id" :user_id,
        "message":message,
        "random_id":0
    }
    if keyboard != None:
        post["keyboard"] = keyboard.get_keyboard()
    else:
        post = post
    vk.method("messages.send",post)
def message(event,keyboard=0,text=2):
    if keyboard == 0:
        vk.messages.send(user_id=event.user_id,message=text, random_id=0)
    else:
        vk.messages.send(user_id=event.user_id, message=text, random_id=0, keyboard=keyboard.get_keyboard())

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.from_user: #Если написали в ЛС
            print('prohlo')
            text = event.text.lower()
            user_id = event.user_id


            if text == 'меню':
                    keyboard = VkKeyboard(one_time=True)
                    keyboard.add_button("1", VkKeyboardColor.POSITIVE)
                    keyboard.add_button("2", VkKeyboardColor.PRIMARY)
                    keyboard.add_button("3", VkKeyboardColor.NEGATIVE)
                    vk.messages.send(user_id=user_id, message='Выберите из меню: \n1)доступные магазины \n2)список желаемых энергетиков\n3)парсер', random_id=0, keyboard=keyboard.get_keyboard())
                    for event in longpoll.listen():

                        if event.type == VkEventType.MESSAGE_NEW:
                            text = event.text.lower()
                            user_id = event.user_id
                            if text == '1':
                                shoptext = ' '.join(shop)
                                message(event,keyboard,f'магазины:\n{shoptext}')
                            if text == '2':
                                message(event,keyboard,'энергетики:(доработка)')
                            if text == '3':
                                product = ['adrenaline','black-monster','burn','drive-me','gorilla','red-bull','tornado']
                                for i in shop:
                                    message(event,text=f'Дружище!Погодь полминутки, пойми, я через мобильный интернет ищу😇')
                                    time.sleep(2)
                                    message(event,text=f'Прогрузил сайт магазина {i.upper()} 🤗')
                                    time.sleep(1)
                                    message(event, text=f'[✔]НАЧАЛ ИСКАТЬ В МАГАЗИНЕ {i.upper()} 😎')
                                    d = start(i,product)
                                    message(event, text=f'Кажется,я что то нашел🧐')
                                    time.sleep(1.5)
                                    message(event,text=f'[✔]НАШЕЛ ЦЕНЫ ДЛЯ МАГАЗИНА {i.upper()}🥺:')
                                    time.sleep(0.5)
                                    message(event,text=d)
                            if text == 'назад':
                                break


            else:
                keyboard = VkKeyboard(one_time=True)
                keyboard.add_button("меню", VkKeyboardColor.PRIMARY)
                vk.messages.send(user_id=event.user_id, random_id=11, message='напиши "меню" и продолжаем',keyboard=keyboard.get_keyboard())
