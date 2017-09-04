import requests
#from time import gmtime, strftime
import sqlite3

def fn():
	url2 = 'https://leprosorium.ru/api/feeds/mixed?per_page=42&threshold_rating=nightmare&page=1'
	hlpr = {'HEADERS!!!'}

	r = requests.get(url2, headers=hlpr)
	p = r.json()

	con = sqlite3.connect('lepra.db')
	cur = con.cursor()

	for psn in p['posts']:
		if psn['golden'] == True :
			cur.execute('SELECT unread_comments_count FROM posts WHERE id = '+ str(psn['id']))
			row = cur.fetchone()
			if row == None:
				body = str(psn['body']).replace('"', '""')
				st = 'INSERT INTO posts (id, rating, created, comments_count, unread_comments_count, href, body) VALUES('+ str(psn['id']) + ', ' + str(psn['rating']) + ', ' + str(psn['created']) + ', ' + str(psn['comments_count']) + ', ' + str(psn['unread_comments_count']) + ', "' + str(psn['_links'][0]['href']) + '", "' + body + '")'
				cur.execute(st)
				con.commit()
				print('inserted', psn['id'])
			else:
				if row[0] != psn['unread_comments_count']:
					cur.execute('UPDATE posts SET unread_comments_count =' + str(psn['unread_comments_count']) + ', comments_count = '+ str(psn['comments_count']) + ', rating = '+ str(psn['rating']) + ' WHERE id = '+ str(psn['id']))
					con.commit()
					print('updated', psn['id'])

	con.close()

if __name__ == "__main__":
	fn()	