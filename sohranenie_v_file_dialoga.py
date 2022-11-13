import autorization
import random
import datetime


def sohranenie_dialoga(object):
    try:
        with open('dialog.txt', 'a',encoding = 'UTF-8') as dialog_file:
            if object['text'] != '[club203978422|@teawithkaguya] Хочу еще арт!':
                if object['text'] != '':
                    dialog_file.write(f"{str(object['text'])}\n")
    except Exception as error:
        print('Ошибка в сохранении диалога: ', error)
        autorization.autorixations_file.session_group.method ( 'messages.send' , {
            'chat_id': str ( 4 ) ,
            'random_id': random.randint ( 0 , 4294967295 ) ,
            'message': f'Ошибка при сохранении обучающих данных! Время: {(datetime.datetime.utcnow () + datetime.timedelta ( hours = 3 )).time ()}'
        } )