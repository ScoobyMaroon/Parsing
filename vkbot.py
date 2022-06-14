import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
vk_session = vk_api.VkApi(token='dfc4a16561b301baf13a27364bff58168642b179ffd762f56221aa1de97960a7ade5833c3aff0513a4786')
from vk_api.longpoll import VkLongPoll, VkEventType
from parsing import create_url,link,start
from vk_api import utils
import time
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
magazin = {'SPAR' : VkKeyboardColor.POSITIVE, 'Окей' : VkKeyboardColor.POSITIVE}
energys = {'adrenaline': VkKeyboardColor.POSITIVE, 'burn': VkKeyboardColor.POSITIVE,
                                           'black monster': VkKeyboardColor.POSITIVE,
                                           'drive me': VkKeyboardColor.POSITIVE, 'gorilla': VkKeyboardColor.POSITIVE,
                                           'red-bull': VkKeyboardColor.POSITIVE,
                                           'tornado': VkKeyboardColor.POSITIVE}
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
def set_list(slovar):
    product = []
    for i in slovar:
        if slovar[i] == VkKeyboardColor.POSITIVE:
            product.append(i)
    return product
def message(event,keyboard=0,text=2):
    if keyboard == 0:
        vk.messages.send(user_id=event.user_id,message=text, random_id=0)
    else:
        vk.messages.send(user_id=event.user_id, message=text, random_id=0, keyboard=keyboard.get_keyboard())
def back_menu(text):
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button("меню", VkKeyboardColor.PRIMARY)
    message(event, keyboard, text)
def generate_list(start='',dictionary={}):
    list = start
    for i in dictionary:
        if dictionary[i] == VkKeyboardColor.POSITIVE:
            list += f'✅{i}\n'
        if dictionary[i] == VkKeyboardColor.NEGATIVE:
            list += f'❌ {i}\n'
    return list
def generate_choice(dictionary):
    b = 0
    for i in dictionary:
        b += 1
        keyboard.add_button(i, dictionary[i])
        if b == 2:
            keyboard.add_line()
            b = 0
    if len(dictionary) % 2 == 0:
        pass
    else:
        keyboard.add_line()
    keyboard.add_button('назад', VkKeyboardColor.PRIMARY)
def set_settings(dictionary,text):
    if dictionary[text]:
        if dictionary[text] == VkKeyboardColor.POSITIVE:
            dictionary[text] = VkKeyboardColor.NEGATIVE
            print(f'[DELETE] Из списка убран {text} ')
        else:
            dictionary[text] = VkKeyboardColor.POSITIVE
            print(f'[ADDED] В список добавлен {text} ')
    return dictionary
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.from_user: #Если написали в ЛС
            user_id = event.user_id
            text = event.text.lower()
            print(f'[INFO] получено новое сообщение от {vk.users.get(user_id=user_id)[0]["first_name"]} {vk.users.get(user_id=user_id)[0]["last_name"]}')
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
                            print(f'[INFO] получено новое сообщение от {vk.users.get(user_id=user_id)[0]["first_name"]} {vk.users.get(user_id=user_id)[0]["last_name"]}')
                            if text == '1':
                                keyboard = VkKeyboard(one_time=True)
                                generate_choice(magazin)
                                spisok = generate_list('Список магазинов,в которых следует искать(кликните по магазинам, которые следует удалить\второй раз добавить):\n',
                                                       magazin)
                                message(event, keyboard, spisok)
                                for event in longpoll.listen():
                                    if event.type == VkEventType.MESSAGE_NEW:
                                        text = event.text
                                        user_id = event.user_id
                                        print(f'[INFO] получено новое сообщение от {vk.users.get(user_id=user_id)[0]["first_name"]} {vk.users.get(user_id=user_id)[0]["last_name"]}')
                                        if text == 'назад':
                                            back_menu('Нажмите меню,чтобы вернутся к выбору')
                                            break
                                        try:
                                            magazin = set_settings(magazin,text)
                                            keyboard = VkKeyboard(one_time=True)
                                            generate_choice(magazin)
                                            spisok = generate_list('Список магазинов, которые следует найти:\n',magazin)
                                            message(event, keyboard, spisok)
                                        except Exception as e:
                                            pass
                            if text == '2':
                                keyboard = VkKeyboard(one_time=True)
                                generate_choice(energys)
                                spisok = generate_list('Список энергетиков, которые следует найти(кликните по маркам, которые следует удалить):\n',energys)
                                message(event, keyboard, spisok)
                                for event in longpoll.listen():
                                    if event.type == VkEventType.MESSAGE_NEW:
                                        text = event.text.lower()
                                        user_id = event.user_id
                                        print(f'[INFO] получено новое сообщение от {vk.users.get(user_id=user_id)[0]["first_name"]} {vk.users.get(user_id=user_id)[0]["last_name"]}')
                                        if text == 'назад':
                                            back_menu('Нажмите меню,чтобы вернутся к выбору')
                                            break
                                        try:
                                            energys = set_settings(energys,text)
                                            keyboard = VkKeyboard(one_time=True)
                                            generate_choice(energys)
                                            spisok = generate_list('Список энергетиков, которые следует найти:\n',energys)
                                            message(event, keyboard, spisok)
                                        except Exception as e:
                                            pass
                            if text == '3':
                                product = set_list(energys)
                                shop = set_list(magazin)
                                if len(product) > 0 and len(shop) > 0:
                                    print(f'[PARSER] PRODUCTS:{product},SHOP:{shop} staring search....')
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
                                    back_menu('Нажмите меню,чтобы вернутся к выбору')
                                    break
                                else:
                                    back_menu('Должен быть выбран хотя бы один магазин и одна марка энергетиков')
                                    break
                            if text == 'назад':
                                break
            else:
                keyboard = VkKeyboard(one_time=True)
                keyboard.add_button("меню", VkKeyboardColor.PRIMARY)
                vk.messages.send(user_id=event.user_id, random_id=11, message='напиши "меню" и продолжаем',keyboard=keyboard.get_keyboard())
