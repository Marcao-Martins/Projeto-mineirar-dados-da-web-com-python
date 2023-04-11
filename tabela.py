import sqlite3
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM frases")
rows = cursor.fetchall()
for row in rows:
    print("ID: {}, Frase: {}".format(row[0], row[1]))
