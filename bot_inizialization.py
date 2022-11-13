import datetime
from better_profanity import profanity
from chatterbot import ChatBot
import autorization
import random


# def otvet_bota(object):
#     try:
#         import main
#         otvet =
#         print('OTVET: ', otvet)
#         return otvet
#     except Exception as eror_gen:
#         print('Ошибка при генерации ответа: ', eror_gen)
#         autorization.autorixations_file.session_group.method ( 'messages.send' , {
#             'chat_id': str ( 4 ) ,
#             'random_id': random.randint ( 0 , 4294967295 ) ,
#             'message': f'Ошибка при генерации ответа! Время: {(datetime.datetime.utcnow () + datetime.timedelta ( hours = 3 )).time ()}'
#         } )