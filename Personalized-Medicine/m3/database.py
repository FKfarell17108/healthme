import sqlite3

def init_db():
    conn = sqlite3.connect('healthme.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            age INTEGER,
            gender TEXT,
            weight REAL,
            height REAL,
            lifestyle_score INTEGER,
            disease_risk INTEGER,
            health_cost REAL,
            email TEXT,
            medical_history TEXT,
            allergies TEXT,
            symptoms TEXT,
            past_treatments TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lifestyle_tips (
            id INTEGER PRIMARY KEY,
            disease_risk INTEGER,
            tip TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS educational_articles (
            id INTEGER PRIMARY KEY,
            title TEXT,
            content TEXT,
            disease_risk INTEGER
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
