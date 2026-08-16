import sqlite3
from datetime import datetime, timedelta

DB_NAME = "bot.db"

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()
    
    # 1. Product category table
    c.execute('''
        CREATE TABLE IF NOT EXISTS product_category (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            is_active BOOLEAN DEFAULT 1
        )
    ''')
    
    # 2. Users table
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER UNIQUE,
            username TEXT,
            full_name TEXT,
            wallet INTEGER DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # 3. Products table
    c.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            price INTEGER NOT NULL,
            duration_days INTEGER NOT NULL,
            category_id INTEGER,
            is_active BOOLEAN DEFAULT 1,
            FOREIGN KEY(category_id) REFERENCES product_category(id)
        )
    ''')
    
    conn.commit()
    conn.close()