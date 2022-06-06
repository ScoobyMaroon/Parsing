import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
vk_session = vk_api.VkApi(token='dfc4a16561b301baf13a27364bff58168642b179ffd762f56221aa1de97960a7ade5833c3aff0513a4786')
from vk_api.longpoll import VkLongPoll, VkEventType
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
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.from_user: #Если написали в ЛС
            print('prohlo')
            text = event.text.lower()
            user_id = event.user_id
            if text == 'start':
                print('prohlo2')
                keyboard = VkKeyboard()
                keyboard.add_button("button", VkKeyboardColor.POSITIVE)
                da = {"user_id":event.user_id,"random_id":0,"message":"text","keyboard":keyboard.get_keyboard()}
                vk_session.method("messages.send",da)

