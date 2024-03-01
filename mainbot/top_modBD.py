from baseBD import connect_bd

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