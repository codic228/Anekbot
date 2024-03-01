from baseBD import connect_bd

def anektime():
    aneki = connect_bd()
    cursor = aneki.cursor()
    cursor.execute('SELECT * FROM viewed WHERE issub >=1 ;')
    info = cursor.fetchall()
    return info

def start_sendingbd():
    aneki = connect_bd()
    cursor = aneki.cursor()
    cursor.execute('UPDATE viewed SET issub = 1 WHERE vuser_id = 535601294;')
    aneki.commit()
    aneki.close()

def stop_sendingbd():
    aneki = connect_bd()
    cursor = aneki.cursor()
    cursor.execute('UPDATE viewed SET issub = 2 WHERE vuser_id = 535601294;')
    aneki.commit()
    aneki.close()