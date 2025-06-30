import sqlite3

with open("db/schema.sql", "r") as f:
    schema = f.read()

conn = sqlite3.connect("db/users.db")
conn.executescript(schema)
conn.commit()
conn.close()
