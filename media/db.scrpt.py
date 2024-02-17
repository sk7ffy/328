import sqlite3

db_name = 'db.sqlite'

conn = None
cursor = None
def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()

def do(query):
    cursor.execute(query)
    conn.commit()

def tables_create():
    open()
    cursor.execute('PRAGMA foreign_keys=on')
    do('''
        CREATE TABLE IF NOT EXISTS news (
            id NTEGER PRIMARY KEY,
            title VARCHAR,
            description VARCHAR,
            image VARCHAR
            class_id INTEGER, FOREIGN KEY (class_id)
        '''
    
    )
    do('''
        CREATE TABLE IF NOT EXISTS class (
            id INTEGER PRIMARY KEY,
            name VARCHAR

            
        '''
    
    )
    close()
def drop_table():
    open()
    do('DROP TABLE IF EXISTS classes')
    do('DROP TABLE IF EXISTS news')

def insert_test_data():
    open()
    cursor.execute('''NSERT INTO news (title,description)VALUES (?,?)'''['admin'])
    conn.commit()

    cursor.execute('''INSERT INTO classes (name) VALUES (?)''', ['sport'])
    conn.commit()

    cursor.execute('''NSERT INTO news (title,description,image,class_id)VALUES (?,?, ?,?,?)'''['NEWS TITLE',
                                                                                                'ssssss',
                                                                                                '1asd'
                                                                                                ])

def show_tables():
    open()
    cursor.execute('''SELECT * FROM news''')
    print(cursor.fetchall())

def show_tables():
    open()
    cursor.execute('''SELECT * FROM class''')
    print(cursor.fetchall())

def get_all_news():
    open()
    cursor.execute('''SELECT news.title news.description,classes.name
                    FROM news INNER JOIN ategories ON news.class_id == classes.id
                        ''')  
    return cursor.fetchall()
def add_news(title,description,image,class_id):
    open()
    cursor.execute('''INSERT INTO news
    (title,description,image,class_id)
    VALUES (?,?,?,?,?)''',[title,descritption,image,class_id])''')

tables_create()
    