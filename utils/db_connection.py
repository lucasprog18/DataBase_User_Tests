import sqlite3
import os

DB_PATH = os.path.join("db", "users.db")

def get_connection():
    # Establishes a connection to the SQLite database with a 5-second timeout
    # Prevents OperationalError: database is locked by allowing brief waiting
    return sqlite3.connect("db/users.db", timeout=5)

def execute_query(query, params=None):
    """Execute a query with optional parameters and commit changes."""
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(query, params or [])
        conn.commit()

def fetch_one(query, params=None):
    """Fetch a single row from the database as a dictionary."""
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(query, params or [])
        result = cur.fetchone()
        if result:
            columns = [col[0] for col in cur.description]
            return dict(zip(columns, result))
        return None

def fetch_all(query, params=None):
    """Fetch all rows for a given query."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query, params or [])
    result = cur.fetchall()
    conn.close()
    return result
