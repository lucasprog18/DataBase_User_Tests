import sqlite3
import os

DB_PATH = os.path.join("db", "users.db")

def get_connection():
    """Establish and return a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def execute_query(query, params=None):
    """Execute a query with optional parameters and commit changes."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query, params or [])
    conn.commit()
    conn.close()

def fetch_one(query, params=None):
    """Fetch a single row from the database."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query, params or [])
    result = cur.fetchone()
    conn.close()
    return result

def fetch_all(query, params=None):
    """Fetch all rows for a given query."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query, params or [])
    result = cur.fetchall()
    conn.close()
    return result
