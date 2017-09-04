import sqlite3


con = sqlite3.connect('lepra.db')
cur = con.cursor()
cur.execute('SELECT id, rating, href, created FROM posts ORDER BY created DESC')

for r in cur.fetchall():
	print (r)
con.close()