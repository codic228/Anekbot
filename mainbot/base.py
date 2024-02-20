import sqlite3
from threading import Lock
import random

def connect_bd():
    return sqlite3.connect('anekdots.db')
def create_table():
    aneki = connect_bd()
    cursor = aneki.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS anekitab (
        anek_id INTEGER PRIMARY KEY,
        anek_name TEXT,
        anek_text TEXT,
        anek_rating INTEGER DEFAULT 0,
        user_id INTEGER,
        complaints INTEGER DEFAULT 0
    );
    ''')

    aneki.commit()
    aneki.close()


def my_anekbd(desired_user_id):
    aneki = connect_bd()
    cursor = aneki.cursor()
    select_query = '''
    SELECT COUNT(*)
    FROM anekitab
    WHERE user_id = ?;
    '''
    cursor.execute(select_query, (desired_user_id,))
    result = cursor.fetchone()
    if result[0] > 0:
        cursor.execute('SELECT anek_name, anek_text FROM anekitab WHERE user_id = ?', (desired_user_id,))
        anekdoti = cursor.fetchall()
        return anekdoti 
    else:
       return(False)

def add_anekbd(title, joke, id):
    aneki = connect_bd()
    cursor = aneki.cursor()
    cursor.execute('''
        INSERT INTO anekitab (anek_name, anek_text,  user_id)
        VALUES (?, ?, ?)
                   ''', (title, joke, id))
    aneki.commit()
    aneki.close()


def delete_anekbd(user_id, anekdot_number):
    aneki = connect_bd()
    cursor = aneki.cursor()

    # Проверить, существует ли анекдот с указанным номером для данного пользователя
    select_query = '''
    SELECT anek_id
    FROM anekitab
    WHERE user_id = ?;
    '''
    cursor.execute(select_query, (user_id,))
    result = cursor.fetchall()

    if len(result) >= anekdot_number:
        # Если анекдот с указанным номером существует, удалить его
        anek_id_to_delete = result[anekdot_number - 1][0]
        delete_query = '''
        DELETE FROM anekitab
        WHERE anek_id = ?;
        '''
        cursor.execute(delete_query, (anek_id_to_delete,))
        aneki.commit()
        aneki.close()
        return True
    else:
        # Анекдот с указанным номером не найден
        aneki.close()
        return False
    

def change_anekbd(user_id, anekdot_number, new_title, new_text):
    aneki = connect_bd()
    cursor = aneki.cursor()

    # Проверить, существует ли анекдот с указанным номером для данного пользователя
    select_query = '''
    SELECT anek_id
    FROM anekitab
    WHERE user_id = ?;
    '''
    cursor.execute(select_query, (user_id,))
    result = cursor.fetchall()
    if len(result) >= anekdot_number:
        # Если анекдот с указанным номером существует, получить его идентификатор
        anek_id_to_update = result[anekdot_number - 1][0]

        # SQL-запрос для обновления заголовка анекдота
        update_query = '''
        UPDATE anekitab
        SET anek_name = ?, anek_text = ?
        WHERE anek_id = ? AND user_id = ?;
        '''

        # Выполнить запрос на обновление
        cursor.execute(update_query, (new_title, new_text, anek_id_to_update, user_id))
        aneki.commit()
        aneki.close()
        return True
    else:
        # Анекдот с указанным номером не найден
        aneki.close()
        return False
    

def random_anek():
    aneki = connect_bd()
    cursor = aneki.cursor()
    cursor.execute('SELECT anek_id, anek_text FROM anekitab ORDER BY RANDOM() LIMIT 1;')
    random_row = cursor.fetchone()  
    return random_row

def random_anek_mark_plus(ran_an_id):
    aneki = connect_bd()
    cursor = aneki.cursor()
    update_query = '''
    UPDATE anekitab
    SET anek_rating = anek_rating + 1
    WHERE anek_id = ?;  -- Условие по id
    '''
    record_id = ran_an_id  # Замените на нужный id
    cursor.execute(update_query, (record_id,))
    aneki.commit()
    aneki.close()


def random_anek_mark_minus(ran_an_id):
    aneki = connect_bd()
    cursor = aneki.cursor()
    update_query = '''
    UPDATE anekitab
    SET anek_rating = anek_rating - 1
    WHERE anek_id = ?;  -- Условие по id
    '''
    record_id = ran_an_id  # Замените на нужный id
    cursor.execute(update_query, (record_id,))
    aneki.commit()
    aneki.close()

def complaints_plus(ran_an_id):
    aneki = connect_bd()
    cursor = aneki.cursor()
    update_query = '''
    UPDATE anekitab
    SET complaints = complaints + 1
    WHERE anek_id = ?;  -- Условие по id
    '''
    record_id = ran_an_id  # Замените на нужный id
    cursor.execute(update_query, (record_id,))
    aneki.commit()
    aneki.close()


def top_anek_bd():
    aneki = connect_bd()
    cursor = aneki.cursor()
    select_query = '''
    SELECT *
    FROM anekitab
    ORDER BY anek_rating DESC
    LIMIT 10;
    '''
    cursor.execute(select_query)
    top_records = cursor.fetchall()
    aneki.close()

    return top_records
    

def top_anek_bd_select(indx):
    aneki = connect_bd()
    cursor = aneki.cursor()
    offset_value = indx
    cursor.execute(f'''
    SELECT *
    FROM anekitab
    ORDER BY anek_rating DESC
    LIMIT 1 OFFSET {offset_value};
    ''')
    top_records = cursor.fetchall()
    aneki.close()
    return top_records