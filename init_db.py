# Script to initialize the SQLite database with the 'users' table schema
# Reads and executes the SQL schema defined in 'db/schema.sql'
# Usage: run `python init_db.py` from the project root directory

import sqlite3

with open("db/schema.sql", "r") as f:
    schema = f.read()

conn = sqlite3.connect("db/users.db")
conn.executescript(schema)
conn.commit()
conn.close()
