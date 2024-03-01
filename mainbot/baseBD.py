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
        user_id INTEGER,
        complaints INTEGER DEFAULT 0
    );
    ''')

    aneki.commit()
    aneki.close()


def create_table1():
    view = connect_bd()
    cursor = view.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS viewed (
            vuser_id INTEGER ,
            vanek_num INTEGER,
            issub INTEGER DEFAULT 0,
            timesub TIME
        );
    ''')

    view.commit()
    view.close()

def add_new_member(user_id):
    aneki = connect_bd()
    cursor = aneki.cursor()
    cursor.execute('SELECT COUNT(*) FROM viewed WHERE vuser_id = ?;', (user_id,))
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.execute('''
        INSERT INTO viewed(vuser_id, vanek_num)
        VALUES (?, 0);
        ''', (user_id,))
        aneki.commit()
    







