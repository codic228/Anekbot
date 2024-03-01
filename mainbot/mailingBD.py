from baseBD import connect_bd

def subscribebd(user_id, time_set):
    aneki = connect_bd()
    cursor = aneki.cursor()
    cursor.execute('UPDATE viewed SET issub = 1 WHERE vuser_id = ?;', (user_id,))
    cursor.execute('UPDATE viewed SET timesub = ? WHERE vuser_id = ?;', (time_set, user_id,))
    aneki.commit()
    aneki.close()

def unsubscribedbd(user_id):
    aneki = connect_bd()
    cursor = aneki.cursor()
    cursor.execute('UPDATE viewed SET issub = 0 WHERE vuser_id = ?;', (user_id,))
    aneki.commit()
    aneki.close()

def check_sub(user_id):
    aneki = connect_bd()
    cursor = aneki.cursor()

    cursor.execute('SELECT issub FROM viewed WHERE vuser_id = ?;', (user_id,))
    result = cursor.fetchone()[0]
    if result == 0:
        return False
    elif result == 1:
        return True