from database.db import get_db

# ADD USER
def register_user(telegram_id, username, full_name):
    conn = get_db()
    c = conn.cursor()
    c.execute(
        "INSERT OR IGNORE INTO users (telegram_id, username, full_name) VALUES (?,?,?)",
        (telegram_id, username, full_name)
    )
    conn.commit()
    conn.close()
