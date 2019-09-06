import sqlite3
import csv

conn = sqlite3.connect('C:\\SQLite\\Budget_Dev.db')
cur = conn.cursor()

#delete all data from the table site that logs URL's
cur.execute("DELETE FROM SITE")
conn.commit()