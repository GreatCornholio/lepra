import sqlite3


con = sqlite3.connect('lepra.db')
cur = con.cursor()
cur.execute('CREATE TABLE posts (id INTEGER PRIMARY KEY, rating INTEGER, created INTEGER, comments_count INTEGER, unread_comments_count INTEGER, href TEXT, body TEXT)')


con.commit()
con.close()