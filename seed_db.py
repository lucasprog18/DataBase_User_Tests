# Script to populate the SQLite 'users' table with initial seed data
# Reads from 'db/seed_users.sql' and executes each INSERT statement
# Usage: run `python seed_db.py` after initializing the schema

import sqlite3

def seed_database():
    with open("db/seed_users.sql", "r") as f:
        seed_script = f.read()

    conn = sqlite3.connect("db/users.db")
    conn.executescript(seed_script)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    seed_database()
