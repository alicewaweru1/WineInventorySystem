import sqlite3

def connect_db():
    """Connect to the SQLite database."""
    conn = sqlite3.connect('wine_inventory.db')
    return conn

def create_tables():
    
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS wines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
            wine_id INTEGER NOT NULL,
            quantity_sold INTEGER NOT NULL,
            total_price REAL NOT NULL,
            sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
