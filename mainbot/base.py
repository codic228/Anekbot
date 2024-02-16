import sqlite3
import random

def connect_db():
    return sqlite3.connect('anekdot_bot.db')

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS anekdots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            joke TEXT,
            category TEXT,
            rating INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def add_anekdot(title, joke, category, rating):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO anekdots (title, joke, category, rating) 
        VALUES (?, ?, ?, ?)
    ''', (title, joke, category, rating))
    conn.commit()
    conn.close()

def get_anekdots():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM anekdots')
    anekdots = cursor.fetchall()
    conn.close()
    return anekdots

def rand_anekdot():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT MAX(id) FROM anekdots')
    last_id = cursor.fetchone()[0]
    rand_id_anek = random.randint(1,last_id)
    cursor.execute('SELECT joke FROM anekdots WHERE id = ?', (rand_id_anek,))
    rand_anekdot = cursor.fetchone()
    conn.close()
    return rand_anekdot

