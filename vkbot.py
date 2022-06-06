import vk_api

vk_session = vk_api.VkApi(token='dfc4a16561b301baf13a27364bff58168642b179ffd762f56221aa1de97960a7ade5833c3aff0513a4786')
from vk_api.longpoll import VkLongPoll, VkEventType
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
   #Слушаем longpoll, если пришло сообщение то:
        if event.from_user: #Если написали в ЛС
            print('prohlo')
            vk.messages.send( #Отправляем сообщение
                user_id=event.user_id,
                random_id=1,
                message='Ваш текст'
		)
