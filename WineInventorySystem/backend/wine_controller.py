from database.db import connect_db

def add_wine(name, description, quantity, price):
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO wines (name, description, quantity, price)
        VALUES (?, ?, ?, ?)
    ''', (name, description, quantity, price))
    conn.commit()
    conn.close()


def get_all_wines():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM wines')
    wines = cursor.fetchall()
    conn.close()
    return wines


def delete_wine(wine_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM wines WHERE id = ?', (wine_id,))
    conn.commit()
    conn.close()
        