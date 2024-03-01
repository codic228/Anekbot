from baseBD import connect_bd

def all_aneksbd():
    aneki = connect_bd()
    cursor = aneki.cursor()
    cursor.execute('SELECT anek_id, anek_name, anek_rating, user_id, complaints FROM anekitab')
    all_an = cursor.fetchall()
    return all_an

def all_usersbd():
    aneki = connect_bd()
    cursor = aneki.cursor()
    cursor.execute('SELECT * FROM viewed')
    all_us = cursor.fetchall()
    return all_us

def show_anekbd(anekdot_number):
    aneki = connect_bd()
    cursor = aneki.cursor()
    # Проверить, существует ли анекдот с указанным номером для данного пользователя
    select_query = '''
    SELECT anek_id
    FROM anekitab;
    '''
    cursor.execute(select_query)
    result = cursor.fetchall()
    if len(result) >= anekdot_number:
        anek_id_to_show = result[anekdot_number - 1][0]
        show_query = '''
        SELECT * FROM anekitab
        WHERE anek_id = ? 
        LIMIT 1;
        '''
        cursor.execute(show_query, (anek_id_to_show,))
        selected_anek = cursor.fetchone()
        aneki.close()
        return selected_anek
    else:
        # Анекдот с указанным номером не найден
        aneki.close()
        return False
    
def moddelete_bd(anekdot_number):
    aneki = connect_bd()
    cursor = aneki.cursor()

    # Проверить, существует ли анекдот с указанным номером для данного пользователя
    select_query = '''
    SELECT anek_id
    FROM anekitab;
    '''
    cursor.execute(select_query)
    result = cursor.fetchall()

    if len(result) >= anekdot_number:
        # Если анекдот с указанным номером существует, удалить его
        anek_id_to_delete = result[anekdot_number - 1][0]
        delete_query = '''
        DELETE FROM anekitab
        WHERE anek_id = ?;
        '''
        cursor.execute(delete_query, (anek_id_to_delete,))
        cursor.execute('UPDATE viewed SET vanek_num = vanek_num - 1 WHERE vanek_num >= ?', (anekdot_number - 1,))
        aneki.commit()
        aneki.close()
        return True
    else:
        # Анекдот с указанным номером не найден
        aneki.close()
        return False
    
def modchange_bd(anekdot_number, new_title, new_text):
    aneki = connect_bd()
    cursor = aneki.cursor()

    # Проверить, существует ли анекдот с указанным номером для данного пользователя
    select_query = '''
    SELECT anek_id
    FROM anekitab;
    '''
    cursor.execute(select_query)
    result = cursor.fetchall()
    if len(result) >= anekdot_number:
        # Если анекдот с указанным номером существует, получить его идентификатор
        anek_id_to_update = result[anekdot_number - 1][0]

        # SQL-запрос для обновления заголовка анекдота
        update_query = '''
        UPDATE anekitab
        SET anek_name = ?, anek_text = ?
        WHERE anek_id = ?;
        '''

        # Выполнить запрос на обновление
        cursor.execute(update_query, (new_title, new_text, anek_id_to_update,))
        aneki.commit()
        aneki.close()
        return True
    else:
        # Анекдот с указанным номером не найден
        aneki.close()
        return False
    