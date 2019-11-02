import menu, find

import pymysql


class DB():
	def __init__(self, host='localhost', port=3306, db='', user='root', password=''):
		self.conn = pymysql.connect(host=host, port=port, db=db, user=user, password=password)
		self.cur = self.conn.cursor()

	def __enter__(self):
		return self.cur

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.conn.commit()
		self.cur.close()
		self.conn.close()

def main():
	while True:
		menu.show_menu()
		i = input('請輸入指令:')
		if i == '1':
			find.sourceIP(db)
		elif i == '2':
			find.timeRange(db)
		elif i == '3':
			find.fQDN(db)
		elif i == 'q':
			exit()
		else:
			print('請輸入正確指令')

if __name__ == '__main__':
	with DB(user='root', password='', db='backendtest') as db:
		main()
