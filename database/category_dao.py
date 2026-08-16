from database.db import get_db

def add_category(name):
    existing_category = get_category_by_name(name)
    if existing_category:
        return existing_category['id']
    conn = get_db()
    c = conn.cursor()
    c.execute("INSERT INTO product_category (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()
    return c.lastrowid

def list_categories():
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT * FROM product_category")
    categories = c.fetchall()
    conn.close()
    return categories

def get_category_by_name(name):
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT * FROM product_category WHERE name = ?", (name,))
    category = c.fetchone()
    conn.close()
    return category