import sqlite3
import csv

conn = sqlite3.connect('C:\\source\\db.sqlite3.db')
cur = conn.cursor()

#delete all data from the table site that logs URL's
cur.execute("DELETE FROM LOCATON")
conn.commit()
