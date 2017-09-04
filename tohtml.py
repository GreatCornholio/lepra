# coding: cp1251
import sqlite3


con = sqlite3.connect('lepra.db')
cur = con.cursor()
cur.execute('SELECT id, rating, href, created, body FROM posts ORDER BY created DESC')

f = open('1.html', 'w', encoding='utf-8')

f.write ('<!DOCTYPE html><html><head><meta charset="utf-8"><title>Смешной заголовок HTML-страницы</title></head><body>')

for r in cur.fetchall():
	f.write(str(r[0]) + '<BR>' + str(r[1]) + '<BR>' + r[2] + '<BR>' + str(r[3]) + '<BR>\n' )
	f.write(r[4])
	f.write('\n<BR><BR>------------------------------------------------------------------------------------------------------------------------------------------<BR><BR>\n\n')

con.close()
f.write('</body></html>')
f.close()