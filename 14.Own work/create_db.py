import sqlite3
from werkzeug.security import generate_password_hash

conn = sqlite3.connect('users.db')
conn.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')
hashed_pw = generate_password_hash('pass123')
conn.execute('INSERT OR IGNORE INTO users (email, password) VALUES (?, ?)',
             ('user@example.com', hashed_pw))
conn.commit()
conn.close()

print("Database & default user created.")
