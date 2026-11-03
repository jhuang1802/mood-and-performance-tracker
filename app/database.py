import sqlite3
from fastapi import HTTPException

def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS moods (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rating INTEGER NOT NULL,
            notes TEXT
            );
        """)

        
def get_connection():
    conn = sqlite3.connect('moods.db')
    conn.row_factory = sqlite3.Row
    return conn
    
def get_all_moods():
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM moods ORDER BY id DESC""")

        rows = cursor.fetchall()
    return rows

def get_mood(id: int):
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM moods WHERE id = ?""", (id,))
        row = cursor.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="ID not found")
        
    return row

def add_mood(rating: int, notes: str):
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO moods (rating, notes) VALUES (?, ?) RETURNING *""", (rating, notes))
        row = cursor.fetchone()
    return row

def delete_mood(id: int):
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""DELETE FROM moods WHERE id = ? RETURNING *""", (id,))
        row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="ID not found")
    return row

def replace_mood(id: int, rating: int, notes: str):
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""UPDATE moods SET rating = ?, notes = ? WHERE id = ? RETURNING *""", (rating, notes, id))
        row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="ID not found")
    return row
