import sqlite3
from threading import Lock

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
        user_id INTEGER
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
    
