import datetime
import random
import autorization.autorixations_file
from vk_api.keyboard import VkKeyboard,VkKeyboardColor

def random_art_ids(object):
    try:
        #получаем айди последних тысячи артов из группы
        keybord = VkKeyboard ( inline = True )
        keybord.add_button ( 'Хочу еще арт!' , color = VkKeyboardColor.POSITIVE )
        #отправляем рандомный арт юзеру
        autorization.autorixations_file.session_group.method ( 'messages.send' , {
            'user_id': str ( object['from_id'] ) ,
            'random_id': random.randint ( 0 , 4294967295 ) ,
            'peer_id': str ( object['peer_id'] ) ,
            'attachment': random_art_all(),
            'message': 'Держи арт🖼' ,
            'reply_to': str ( object['id'] ),
            'keyboard':keybord.get_keyboard()
        } )
        del keybord
    except Exception as error:
        print('Ошибка в блоке отправки рандомного арта: ', error)
        autorization.autorixations_file.session_group.method ( 'messages.send' , {
            'chat_id': str ( 4 ) ,
            'random_id': random.randint ( 0 , 4294967295 ) ,
            'message': f'Ошибка при конфигурации рандомного арту! Время: {(datetime.datetime.utcnow () + datetime.timedelta ( hours = 3 )).time ()}'
        } )

def random_art_all():
    ids_fotos = []
    fotos = autorization.autorixations_file.session_kupriyashin.method ( 'photos.get' , {
        'owner_id': str ( '-' + str ( autorization.autorixations_file.chai_group_id ) ) ,
        'album_id': 'wall' ,
        'rev': '1' ,
        'count': '500'
    } )['items']
    for elem in fotos:
        ids_fotos.append ( elem['id'] )
    del fotos
    ids_fotos = ids_fotos[random.randint(0,len(ids_fotos))]
    return f"photo-203978422_{ids_fotos}"