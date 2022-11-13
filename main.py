import datetime
import json
import math
import random
import sqlite3
from chatterbot.response_selection import get_most_frequent_response
from tqdm import tqdm

from vk_api.bot_longpoll import *
from chatterbot import ChatBot

import autorization
from otpravka_pozdravleniya import users_holly_day
from chatterbot.trainers import ListTrainer

otpravka_pozdravleniya = 1 #флаг используемый для отправки поздравления пользователю
bot_inizial = 1 #флаг для перезапуска бота

Bot = ChatBot (
        'Tea_with_Kaguya' ,
        storage_adapter = 'chatterbot.storage.SQLStorageAdapter' ,
        response_selection_method=get_most_frequent_response,
        database_uri = 'sqlite:///database.sqlite3'
    )
print ( 'Инициализация произведена' )

trainer = ListTrainer(Bot)
with open(r'answer_databse/обучение бота песни.txt','r',encoding = 'UTF-8') as data:
    for line in tqdm(data):
        print('----------')
        print(str(line).split('/'))
        trainer.train(str(line).split('/'))




# def otvet_comments(object):
#     print(object)
#     print ( '-----------------------' )
#     try:
#         if 'скрипт' in str(object['text']).lower():#если чувак хочет получить скрипт
#
#             info_user = autorization.autorixations_file.session_kupriyashin.method('users.get',{
#                 'user_ids': str(object['from_id']),
#                 'fields': 'screen_name'
#             })
#             info_user = '@' + info_user[0]['screen_name'] + '(' + info_user[0]['first_name'] + ')' + ', ' #получение обращения к пользователю
#             #отправка комментария
#
#             autorization.autorixations_file.session_group.method('wall.createComment',{
#                 'owner_id': str(object['owner_id']),
#                 'post_id': str(object['post_id']),
#                 'from_group': str(autorization.autorixations_file.chai_group_id),
#                 'reply_to_comment': str(object['id']),
#                 'message': info_user + "Вот ссылочка для доступа:\n"
#                                        "__________________________________________\n"
#                                        " https://disk.yandex.ru/d/zms3GkrvzmHplw🖥\n"
#                                        "__________________________________________\n"
#             })
#             del info_user
#
#         # elif '[club203978422|かぐや茶 Чай с Кагуей],' in object['text'] and str(object['text']).split('[club203978422|かぐや茶 Чай с Кагуей],')[0] == '': #если чувак ответил комментом без текста на сообщение сообщества
#         #     with open('stikers_id.txt','r',encoding = 'UTF-8') as stikers_ids:
#         #         lines = stikers_ids.readlines()
#         #         stiker_id = int(lines[random.randint(0,len(lines))].replace('\n',''))
#         #         del lines
#         #     autorization.autorixations_file.session_group.method ( 'wall.createComment' , {
#         #         'owner_id': str ( object['owner_id'] ) ,
#         #         'post_id': str ( object['post_id'] ) ,
#         #         'from_group': str ( autorization.autorixations_file.chai_group_id ) ,
#         #         'reply_to_comment': str ( object['id'] ) ,
#         #         'sticker_id': str(stiker_id)
#         #     } )
#         #     del stiker_id
#
#         elif object['text'] == '':#если чувак просто написал коммент без текста
#             with open('stikers_id.txt','r',encoding = 'UTF-8') as stikers_ids:
#                 lines = stikers_ids.readlines()
#                 stiker_id = int(lines[random.randint(0,len(lines))].replace('\n',''))
#                 del lines
#             autorization.autorixations_file.session_group.method ( 'wall.createComment' , {
#                 'owner_id': str ( object['owner_id'] ) ,
#                 'post_id': str ( object['post_id'] ) ,
#                 'from_group': str ( autorization.autorixations_file.chai_group_id ) ,
#                 'reply_to_comment': str ( object['id'] ) ,
#                 'sticker_id': str(stiker_id)
#             } )
#             del stiker_id
#
#         elif 'фот' in str(object['text']).lower() or 'арт' in str(object['text']).lower() or 'крас' in str(object['text']).lower(): #если кто-то написал упоминание картинки
#             info_user = autorization.autorixations_file.session_kupriyashin.method ( 'users.get' , {
#                 'user_ids': str ( object['from_id'] ) ,
#                 'fields': 'screen_name'
#             } )
#             info_user = '@' + info_user[0]['screen_name'] + '(' + info_user[0][
#                 'first_name'] + ')' + ', '  # получение обращения к пользователю
#
#             import poluchenie_randomnogo_arta
#             autorization.autorixations_file.session_group.method ( 'wall.createComment' , {
#                 'owner_id': str ( object['owner_id'] ) ,
#                 'post_id': str ( object['post_id'] ) ,
#                 'from_group': str ( autorization.autorixations_file.chai_group_id ) ,
#                 'reply_to_comment': str ( object['id'] ) ,
#                 'message': info_user + 'Держи картиночку😏',
#                 'attachments': poluchenie_randomnogo_arta.random_art_all()
#             } )
#             del info_user
#         else:#если чувак написал какой то текст, ему должен ответить бот
#
#             info_user = autorization.autorixations_file.session_kupriyashin.method ( 'users.get' , {
#                 'user_ids': str ( object['from_id'] ) ,
#                 'fields': 'screen_name'
#             } )
#             info_user = '@' + info_user[0]['screen_name'] + '(' + info_user[0][
#                 'first_name'] + ')' + ', '  # получение обращения к пользователю
#
#             from better_profanity import profanity
#             autorization.autorixations_file.session_group.method ( 'wall.createComment' , {
#                 'owner_id': str ( object['owner_id'] ) ,
#                 'post_id': str ( object['post_id'] ) ,
#                 'from_group': str ( autorization.autorixations_file.chai_group_id ) ,
#                 'reply_to_comment': str ( object['id'] ) ,
#                 'message': info_user + str(profanity.censor(str(Bot.get_response ( str(object['text']) )),'😄'))
#             } )
#             del info_user
#     except Exception as error:
#         print('Ошибка в функции ответа на комментарии: ', error)
#         autorization.autorixations_file.session_group.method ( 'messages.send' , {
#             'chat_id': str ( 8 ) ,
#             'random_id': random.randint ( 0 , 4294967295 ) ,
#             'message': f'Ошибка при отправке комментария! Время: {(datetime.datetime.utcnow () + datetime.timedelta ( hours = 3 )).time ()}'
#         } )
#
# def otvet_ls(object):
#     try:
#         print(object)
#         if str(object['text']).lower() == 'начать':#если пользвоатель пишет впервые
#
#             text_ls_privet = "Дарова✋\n Я умный бот *teawithkaguya (かぐや茶 Чай с Кагуей) и я умею следующее: \n" \
#                              "\n" \
#                              "1⃣. Так как я очень умный - ты можешь со мной просто пообщаться🖊\n" \
#                              "2⃣. Ты можешь получить рандомную картинку командой - Чай дай арт\n" \
#                              "3⃣. Если ты хочешь получить БЕСПЛАТНО СТИКЕРЫ, то вот ссылочка - https://vk.com/@teawithkaguya-kak-poluchit-stikery-vkontakte-besplatno\n" \
#                              "4⃣. Если ты за скриптами, то вот ссылка - https://vk.com/@teawithkaguya-skript-dlya-massovogo-dobavleniya-druzei-v-besedu2022\n" \
#                              "\n" \
#                              "Удачи😏 и пообщайся со мной!"
#             autorization.autorixations_file.session_group.method('messages.send',{
#                 'user_id': str(object['from_id']),
#                 'random_id': random.randint(0,4294967295),
#                 'peer_id':str(object['peer_id']),
#                 'message':text_ls_privet,
#                 'reply_to':str(object['id'])
#             })
#             del text_ls_privet
#
#         elif object['text'] == '': #если в сообщении нет текст кидает стикер
#             with open('stikers_id.txt','r',encoding = 'UTF-8') as stikers_ids:
#                 lines = stikers_ids.readlines()
#                 stiker_id = int(lines[random.randint(0,len(lines))].replace('\n',''))
#                 del lines
#             autorization.autorixations_file.session_group.method ( 'messages.send' , {
#                 'user_id': str ( object['from_id'] ) ,
#                 'random_id': random.randint ( 0 , 4294967295 ) ,
#                 'peer_id': str ( object['peer_id'] ) ,
#                 'sticker_id': stiker_id,
#                 'reply_to': str ( object['id'] )
#             } )
#             del stiker_id
#
#         elif 'арт' in str(object['text']).lower() or 'картин' in str(object['text']).lower() or 'фот' in str(object['text']).lower(): #если пользователь просит рандомный арт
#             import poluchenie_randomnogo_arta
#             poluchenie_randomnogo_arta.random_art_ids(object)
#
#         else: #если в сообщении имеется текст отвечает бот
#             from better_profanity import profanity
#             autorization.autorixations_file.session_group.method ( 'messages.send' , {
#                 'user_id': str ( object['from_id'] ) ,
#                 'random_id': random.randint ( 0 , 4294967295 ) ,
#                 'peer_id': str ( object['peer_id'] ) ,
#                 'message': str(profanity.censor(str(Bot.get_response ( str(object['text']) )),'😄')) ,
#                 'reply_to': str ( object['id'] )
#             } )
#     except Exception as error:
#         print('Произошла ошибка в блоке ответа на личное сообщение: ', error)
#         autorization.autorixations_file.session_group.method ( 'messages.send' , {
#             'chat_id': str ( 8 ) ,
#             'random_id': random.randint ( 0 , 4294967295 ) ,
#             'message': f'Ошибка при ответе бота в лс групы! Время: {(datetime.datetime.utcnow () + datetime.timedelta ( hours = 3 )).time ()}'
#         } )
#
# def otvet_bota_in_beseda(object):
#     try:
#         # print(object)
#         if 'action' in object : #если произеш акшен добавления в новую беседу
#             if (object['action']['type'] == 'chat_invite_user') and (object['action']['member_id'] == -203978422) :
#                 print('Бота пригласили в чат!')
#                 print(object)
#                 print('-------------------')
#
#                 autorization.autorixations_file.session_group.method('messages.send',{
#                     'random_id': str(random.randint(0,4294967295)),
#                     'chat_id': str(object['peer_id']-2000000000),
#                     'message': "Для нормального функционирования мне необходимо ПРЕДОСТАВИТЬ ДОСТУП К ПЕРЕПИСКЕ (это можно сделать в настройках беседы)"
#                                " \n"
#                                "\nМОЙ ФУНКЦИОНАЛ🧙🏿:\n"
#                                "👉Шанс ответа на сообщение - Чай шанс {1..100}, по умолчанию значение = 5\n"
#                                "Где 1 - отвечается на каждое сообщение, \n100 - отвечает раз в 100 сообщений\n"
#                                "📝Пример: Чай шанс 20 - ответит на 1 из 20 сообщений\n"
#                                "\n👉Рандомный арт - Чай арт\n"
#                                "📝Отправляет рандомную картинку в аниме стилистике (вместо арт можно использовать: фото, картинка, арт, фотка...)"
#                 })
#                 #если группу добавили в новый чат, то добавляет этот чат в базу данных
#                 with sqlite3.Connection('besedi/ids_besed.sqlite3') as id_besed:
#                     cursor = id_besed.cursor()
#                     # cursor.execute("""
#                     # CREATE TABLE besedi(
#                     # id_besedi INTEGER PRIMARY KEY,
#                     # chance INTEGER DEFAULT 5
#                     # );
#                     # """)
#                     try:
#                         cursor.execute("""
#                         INSERT OR IGNORE INTO besedi (id_besedi) VALUES (?);
#                         """, (object['peer_id']-2000000000,))
#                     except Exception as sqlerror:
#                         print('Ошибка при добавлении айди беседы в базу: ', sqlerror)
#
#         elif str(object['text']).lower() == 'приветствие':#если нужно вывести приветствие
#             autorization.autorixations_file.session_group.method ( 'messages.send' , {
#                 'random_id': str ( random.randint ( 0 , 4294967295 ) ) ,
#                 'chat_id': str ( object['peer_id'] - 2000000000 ) ,
#                 'message': "Для нормального функционирования мне необходимо ПРЕДОСТАВИТЬ ДОСТУП К ПЕРЕПИСКЕ (это можно сделать в настройках беседы)"
#                                " \n"
#                                "\nМОЙ ФУНКЦИОНАЛ🧙🏿:\n"
#                                "👉Шанс ответа на сообщение - Чай шанс {1..100}, по умолчанию значение = 5\n"
#                                "Где 1 - отвечается на каждое сообщение, \n100 - отвечает раз в 100 сообщений\n"
#                                "📝Пример: Чай шанс 20 - ответит на 1 из 20 сообщений\n"
#                                "\n👉Рандомный арт - Чай арт\n"
#                                "📝Отправляет рандомную картинку в аниме стилистике (вместо арт можно использовать: фото, картинка, арт, фотка...)"
#                 } )
#
#         # если пользвоатель просит картинку
#         elif ('фот' in str(object['text']).lower() or 'арт' in str(object['text']).lower() or 'изо' in str(object['text']).lower()) and (len(str(object['text']))<150):
#             from vk_api.keyboard import VkKeyboard
#             keybord = VkKeyboard(inline = True)
#             from vk_api.keyboard import VkKeyboardColor
#             keybord.add_button('Хочу еще арт!',color = VkKeyboardColor.POSITIVE)
#             import poluchenie_randomnogo_arta
#             # print(object)
#             try:
#                 forward_message = {"peer_id": object['peer_id'], "conversation_message_ids": [object['conversation_message_id']], "reply_to": 1 }
#                 autorization.autorixations_file.session_group.method('messages.send',{
#                     'chat_id': str(object['peer_id']-2000000000),
#                     'message': 'Смотрите, что накопал❤',
#                     'random_id': str(random.randint ( 0 , 4294967295 )) ,
#                     # 'reply_to': str(object['conversation_message_id']),
#                     'attachment': poluchenie_randomnogo_arta.random_art_all(),
#                     'keyboard':keybord.get_keyboard(),
#                     'forward': json.dumps(forward_message),
#                     'disable_mentions': str ( 0 )
#                 })
#             except Exception as error_mes:
#                 print('ОШибка при ответе на сообщение: ', error_mes)
#             del keybord
#             del forward_message
#         elif object['text'] == '':# если нет текста (стикер, картинка изображение и т.д.)
#             with sqlite3.connect('besedi/ids_besed.sqlite3') as db:#получает шанс отправки сообщения
#                 cursor = db.cursor()
#                 out_range_random = cursor.execute("""
#                     SELECT chance FROM besedi WHERE id_besedi = ?;
#                 """,(object['peer_id']-2000000000,))
#                 out_range_random = out_range_random.fetchone()[0]
#
#             if random.randint(1,out_range_random) == out_range_random:
#                 if random.randint(1,out_range_random) == out_range_random:#если получено определенное значение кидает картинку
#
#                     from vk_api.keyboard import VkKeyboard
#                     keybord = VkKeyboard ( inline = True )
#                     from vk_api.keyboard import VkKeyboardColor
#                     keybord.add_button ( 'Может еще артик😏' , color = VkKeyboardColor.POSITIVE )
#                     print('Отправляю картинку')
#                     import poluchenie_randomnogo_arta
#                     forward_message = {"peer_id": object['peer_id'] ,
#                                        "conversation_message_ids": [object['conversation_message_id']] , "reply_to": 1}
#                     autorization.autorixations_file.session_group.method ( 'messages.send' , {
#                         'chat_id': str ( object['peer_id'] - 2000000000 ) ,
#                         # 'message': 'Смотрите, что накопал❤' ,
#                         'random_id': str ( random.randint ( 0 , 4294967295 ) ) ,
#                         # 'reply_to': str(object['conversation_message_id']),
#                         'attachment': poluchenie_randomnogo_arta.random_art_all (),
#                         'keyboard': keybord.get_keyboard () ,
#                         'forward': json.dumps ( forward_message ),
#                         'disable_mentions': str ( 0 )
#                     } )
#                     del keybord
#                     del forward_message
#                 elif random.randint(1,out_range_random) == 1: #если значение равно другому определенному то стикер
#                     print('Отправляю стикер')
#                     with open ( 'stikers_id.txt' , 'r' , encoding = 'UTF-8' ) as stikers_ids:
#                         lines = stikers_ids.readlines ()
#                         stiker_id = int ( lines[random.randint ( 0 , len ( lines ) )].replace ( '\n' , '' ) )
#                         del lines
#                     forward_message = {"peer_id": object['peer_id'] ,
#                                        "conversation_message_ids": [object['conversation_message_id']] , "reply_to": 1}
#                     autorization.autorixations_file.session_group.method ( 'messages.send' , {
#                         'chat_id': str ( object['peer_id'] - 2000000000 ) ,
#                         'random_id': random.randint ( 0 , 4294967295 ) ,
#                         'sticker_id': stiker_id,
#                         'forward': json.dumps ( forward_message ),
#                         'disable_mentions': str(0)
#                     } )
#                     del forward_message
#                     del stiker_id
#                 del out_range_random
#
#         elif 'чай шанс' in str(object['text']).lower():#если хотят сменить шанс ответа
#             if str(object['text']).split(' ')[2].isdigit() :#проверка на дурака
#                 chance = int(str(object['text']).split(' ')[2])
#                 if chance < 1 or chance > 100:# проверка на вхождение в диапазон
#                     print('Шанс: ', str(object['text']).split(' ')[2])
#                     forward_message = {"peer_id": object['peer_id'] ,
#                                        "conversation_message_ids": [object['conversation_message_id']] ,
#                                        "reply_to": 1}
#                     autorization.autorixations_file.session_group.method ( 'messages.send' , {
#                         'chat_id': str ( object['peer_id'] - 2000000000 ) ,
#                         'random_id': random.randint ( 0 , 4294967295 ) ,
#                         'message': 'Неверный диапазон! 1 < N < 100',
#                         'forward': json.dumps ( forward_message ),
#                         'disable_mentions': str ( 0 )
#                     } )
#                     del forward_message
#                 else:
#                     try:
#                         with sqlite3.connect('besedi/ids_besed.sqlite3') as bd:
#                             cursor = bd.cursor()
#                             cursor.execute("""
#                             UPDATE besedi SET chance = ? WHERE id_besedi = ?;
#                             """,(chance,object['peer_id']-2000000000))
#
#                         forward_message = {"peer_id": object['peer_id'] ,
#                                            "conversation_message_ids": [object['conversation_message_id']] ,
#                                            "reply_to": 1}
#                         autorization.autorixations_file.session_group.method ( 'messages.send' , {
#                             'chat_id': str ( object['peer_id'] - 2000000000 ) ,
#                             'random_id': random.randint ( 0 , 4294967295 ) ,
#                             'message': "Шанс успешно обновлен!",
#                             'forward': json.dumps ( forward_message ),
#                             'disable_mentions': str ( 0 )
#                         } )
#                         del forward_message
#                     except Exception as sqlerror:
#                         print('Ошибка при обновлении шанса: ', sqlerror)
#                         autorization.autorixations_file.session_group.method ( 'messages.send' , {
#                             'chat_id': str ( object['peer_id'] - 2000000000 ) ,
#                             'random_id': random.randint ( 0 , 4294967295 ) ,
#                             'message': 'Ошибка при обновлении шанса ответа, свяжитесь с администратором!'
#                         } )
#             else:
#                 forward_message = {"peer_id": object['peer_id'] ,
#                                    "conversation_message_ids": [object['conversation_message_id']] ,
#                                    "reply_to": 1}
#                 autorization.autorixations_file.session_group.method ( 'messages.send' , {
#                     'chat_id': str ( object['peer_id'] - 2000000000 ) ,
#                     'random_id': random.randint ( 0 , 4294967295 ) ,
#                     'message': 'Фраза написана НЕ верно!',
#                     'forward': json.dumps ( forward_message ),
#                     'disable_mentions': str ( 0 )
#                 } )
#                 del forward_message
#         else:
#             try:
#                 print(object)
#                 with sqlite3.connect('besedi/ids_besed.sqlite3') as db:#получает шанс отправки сообщения
#                     cursor = db.cursor()
#                     out_range_random = cursor.execute("""
#                         SELECT chance FROM besedi WHERE id_besedi = ?;
#                     """,(object['peer_id']-2000000000,))
#                     out_range_random = out_range_random.fetchone()[0]
#
#                 if 'reply_message' in object:
#                     if object['reply_message']['from_id'] == -203978422:
#                         from better_profanity import profanity
#                         forward_message = {"peer_id": object['peer_id'] ,
#                                            "conversation_message_ids": [object['conversation_message_id']] ,
#                                            "reply_to": 1}
#                         autorization.autorixations_file.session_group.method ( 'messages.send' , {
#                             'chat_id': str ( object['peer_id'] - 2000000000 ) ,
#                             'random_id': str ( random.randint ( 0 , 4294967295 ) ) ,
#                             'message': str (
#                                 profanity.censor ( str ( Bot.get_response ( str ( object['text'] ) ) ) , '😄' ) ) ,
#                             'forward': json.dumps ( forward_message ) ,
#                             'disable_mentions': str ( 0 )
#                         } )
#                         from sohranenie_v_file_dialoga import sohranenie_dialoga
#                         # print(object)
#                         sohranenie_dialoga ( object )
#                         del forward_message
#
#                 elif random.randint(1,out_range_random) == 1:
#                     print(object)
#                     from better_profanity import profanity
#                     forward_message = {"peer_id": object['peer_id'] ,
#                                        "conversation_message_ids": [object['conversation_message_id']] , "reply_to": 1}
#                     autorization.autorixations_file.session_group.method ( 'messages.send' , {
#                         'chat_id': str ( object['peer_id'] - 2000000000 ) ,
#                         'random_id': str(random.randint ( 0 , 4294967295 )) ,
#                         'message': str(profanity.censor(str(Bot.get_response ( str(object['text']) )),'😄')),
#                         'forward': json.dumps ( forward_message ),
#                         'disable_mentions': str ( 0 )
#                     } )
#                     from sohranenie_v_file_dialoga import sohranenie_dialoga
#                     # print(object)
#                     sohranenie_dialoga ( object )
#                     del forward_message
#                 del out_range_random
#
#             except Exception as ror:
#                 print("Ошибка при ответе бота: ", ror)
#                 autorization.autorixations_file.session_group.method ( 'messages.send' , {
#                     'chat_id': str ( 8 ) ,
#                     'random_id': random.randint ( 0 , 4294967295 ) ,
#                     'message': f'Ошибка при ответе бота в беседу! Время: {(datetime.datetime.utcnow () + datetime.timedelta ( hours = 3 )).time ()}'
#                 } )
#     except Exception as error:
#         print('Ошибка в модуле ответа в беседу: ',error)
#         autorization.autorixations_file.session_group.method ( 'messages.send' , {
#             'chat_id': str ( 8 ) ,
#             'random_id': random.randint ( 0 , 4294967295 ) ,
#             'message': f'Ошибка в модуле отправки ответа в беседу! Время: {(datetime.datetime.utcnow () + datetime.timedelta ( hours = 3 )).time ()}'
#         } )
#
# while True:
#     #Слушаем сервер на предмет событий
#     for event in VkBotLongPoll(autorization.autorixations_file.session_group, group_id = int(autorization.autorixations_file.chai_group_id), wait = 30).listen():
#         # print(event.type)
#         time_now = (datetime.datetime.utcnow()+datetime.timedelta(hours = 3)).time()
#
#         if time_now.hour == 20 and otpravka_pozdravleniya == 1: #если время 12 часов дня и флаг равен 1
#             users_holly_day()
#             otpravka_pozdravleniya = 0 #обнуляем флаг, чтобы не было еще одной отправки
#         if time_now.hour in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,22,23]:#разрешаем отправку на следующий день
#             otpravka_pozdravleniya = 1
#
#         # if time_now.hour == 19 and bot_inizial != 0:#обучает бота
#         #     sohranenie_v_file_dialoga.obuchenie_iz_file()
#         # if time_now.hour in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,22,23]:#устанавливаем флаг переинициализации в 0
#         #     bot_inizial = 1
#
#         if event.type == VkBotEventType.WALL_REPLY_NEW: #комментарий на стене
#             if event.object['from_id']>0:#оставляет комментарий человек, а не группа
#                 otvet_comments(event.object)#переходим в файл для ответа на комментарий в сообществе
#
#         if event.type == VkBotEventType.MESSAGE_NEW:#сообщение в сообществе или беседе
#             if event.object['message']['from_id']>0:#пишет не группа, а пользователь
#                 if event.object['message']['peer_id'] > 2000000000: #значит пришло сообщение из беседы
#                     otvet_bota_in_beseda(event.object['message'])
#                 else:#пришло сообщение в лс
#                      otvet_ls(event.object['message'])#переходим в файл otvet_v_ls_gruppi.py и выполняем функцию ответа