from baseBD import connect_bd

def act_not_random_anek(user_id):
    aneki = connect_bd()
    cursor = aneki.cursor()
    cursor.execute('SELECT COUNT(*) FROM anekitab')
    anek_count = cursor.fetchone()[0]
    if anek_count == 0:
        return True
    else:
        cursor.execute('SELECT vanek_num FROM viewed WHERE vuser_id = ?', (user_id,))
        anek_num = cursor.fetchone()[0]
        if anek_count == anek_num:
            return False
        elif anek_count > anek_num:
            cursor.execute('SELECT anek_id, anek_name, anek_text FROM anekitab LIMIT 1 OFFSET (SELECT vanek_num FROM viewed WHERE vuser_id = ?);', (user_id,))
            anek = cursor.fetchone()
            cursor.execute('UPDATE viewed SET vanek_num = vanek_num + 1 WHERE vuser_id = ?', (user_id,))
            aneki.commit()
            return anek



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