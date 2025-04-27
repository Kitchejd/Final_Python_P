import sqlite3

conn = sqlite3.connect('table_update.db')

cusor = conn.cursor()

cusor.execute('''CREATE TABLE IF NOT EXISTS data_table (id INTEGER PRIMARY KEY, info TEXT, updated_at TIMESTAMP)''')

conn.commit()