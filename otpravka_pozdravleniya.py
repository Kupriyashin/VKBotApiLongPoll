import datetime
import math
import time
from random import randint
import autorization

import tqdm

from autorization.autorixations_file import session_group
from autorization.autorixations_file import chai_group_id
from autorization.autorixations_file import session_kupriyashin

file_ids_fotos_dr = []

def random_foto_dlya_dr():
    fotos = session_kupriyashin.method('photos.get',{
        'owner_id':-int(chai_group_id),
        'album_id':str(287071769),
        'count': 1000
    })['items']
    for ids in tqdm.tqdm(fotos):
        file_ids_fotos_dr.append(ids['id'])
    del fotos


def users_holly_day():
    try:
        count = session_group.method ( 'groups.getMembers' , { #количество пользователей в группе
            'group_id': str ( chai_group_id )
        } )['count']
        # print
        item = []
        for elem in tqdm.tqdm ( range ( math.ceil ( int ( count ) / 100 ) ) ):
            item = session_group.method ( 'groups.getMembers' , {
                'group_id': str(chai_group_id) ,
                'offset': elem * 100 ,
                'count': 100 ,
                'fields': 'bdate'
            } )['items']

        random_foto_dlya_dr ()

        for i in tqdm.tqdm ( range ( len ( item ) ) ):
            if 'bdate' in item[i]:

                if ((int ( item[i]['bdate'].split ( '.' )[0] )) == datetime.datetime.now ().day) and (
                        (int ( item[i]['bdate'].split ( '.' )[1] )) == datetime.datetime.now ().month):
                    print ( f"\nСегодня др у {item[i]['id']}" )

                    session_group.method ( 'wall.createComment' , {
                        'owner_id': -int(chai_group_id) ,
                        'post_id': 9433 ,
                        'from_group': chai_group_id ,
                        'message': f"Сегодня свой день рождения празднует @id{item[i]['id']}({item[i]['first_name']}), поздравляю тебя с днем рождения!"
                                   + "\nЖелаю, чтобы в этот день сбылись все твои мечты!☺" ,
                        'attachments': f"photo-203978422_{file_ids_fotos_dr[randint ( 0 , len ( file_ids_fotos_dr ) - 1 )]}"
                    } )
                    time.sleep ( 0.1 )
        time.sleep ( 0.1 )
        del item
        print ( 'Скрипт завершен' )
    except Exception as error:
        print('Ошибка при отправке поздравления', error)
        autorization.autorixations_file.session_group.method ( 'messages.send' , {
            'chat_id': str ( 4 ) ,
            'random_id': randint ( 0 , 4294967295 ) ,
            'message': f'Поздравление не было отправлено! Время: {(datetime.datetime.utcnow()+datetime.timedelta(hours = 3)).time()}'
        } )
