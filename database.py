import sqlite3
import json

DB_NAME = "data.db"


def initialize_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS data_store (
        id TEXT PRIMARY KEY,
        data TEXT NOT NULL
    )
    """
    )
    conn.commit()
    conn.close()


def save_data(key, value):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    json_data = json.dumps(value)
    cursor.execute(
        """
    INSERT OR REPLACE INTO data_store (id, data) VALUES (?, ?)
    """,
        (key, json_data),
    )
    conn.commit()
    conn.close()
    print(f"Дані успішно збережені для ключа: {key}")


def get_data(key):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT data FROM data_store WHERE id = ?", (key,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return json.loads(row[0])
    else:
        print(f"Дані для ключа {key} не знайдено.")
        return None
