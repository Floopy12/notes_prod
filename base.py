import sqlite3 as sq

with sq.connect('note.bd') as con:
    con.row_factory = lambda cursor, row: row[0]
    cur = con.cursor()

    
# cur.execute('DROP TABLE IF EXISTS note')

cur.execute('''CREATE TABLE IF NOT EXISTS note(
    note_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    content TEXT NOT NULL
    )''')