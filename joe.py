import vk_api
import re
import os
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

#VARIABLES
token = os.environ['TOKEN']
pistol = re.compile('!пистоль .*')
vk_session = vk_api.VkApi(token='{}'.format(token))
longpoll = VkBotLongPoll(vk_session, 202317834)
vk = vk_session.get_api()

#Send message function
def send_msg(message='', attachment=''):
    return vk.messages.send(peer_id=event.obj.peer_id, message=message, attachment=attachment, random_id=get_random_id())

#Check events and make corresponding actions
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.object.text == '!Роман':
            send_msg(message='Не тупой!')
        if event.object.text == '!Андрюша':
            send_msg(message='Детский врач')
        if event.object.text == '!Славик':
            send_msg(message='Опять проспал')
        if pistol.match(event.object.text):
            name = event.object.text
            name = name.split()[1]
            #name = vk.users.get(user_ids=event.obj.from_id)
            #name = name[0]
            #name = name['first_name'] 
            send_msg(message='БАХ!\nПокойся с миром, {}...'.format(name))
        if event.object.text == '!баскет':
            send_msg(attachment='photo-202317834_457239017')
