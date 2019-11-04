


def sourceIP(db):
	i = input('請輸入SourceIP:')
	sql = '''select Date, time, usec, SourceIP, SourcePort, DestinationIP, DestinationPort, FQDN 
		from test where SourceIP = '%s' order by Date, time, usec;''' % i
	db.execute(sql)
	rows = db.fetchall()
	page = 1
	pages = len(rows) // 50
	pages += 1
	while True:
		if page > pages:
			break
		print('+----------+----------+-------+-----------------+------------+-----------------+-----------------+----------------------------------------------------------+')
		print('| Date     | time     | usec  | SourceIP        | SourcePort | DestinationIP   | DestinationPort | FQDN                                                     |')
		print('+----------+----------+-------+-----------------+------------+-----------------+-----------------+----------------------------------------------------------+')
		for row in rows[(page-1)*50: page*50]:
			print('| '+row[0]+' | '+row[1]+' | %5s '%row[2]+'| %15s '%row[3]+'| %10s '%row[4]+'| %15s '%row[5]+'| %15s '%row[6]+'| %56s |'%row[7])
		print('+----------+----------+-------+-----------------+------------+-----------------+-----------------+----------------------------------------------------------+')
		print('第 %d 頁 / 共 %d 頁' % (page, pages))
		if pages == 1:
			while True:
				turnpage = input('請輸入q回到menu:')
				if turnpage == 'q':
					page += 1
					break
				else:
					print('請輸入正確指令')
		elif page == 1:
			while True:
				turnpage = input('請輸入d至下一頁:')
				if turnpage == 'd':
					page += 1
					break
				else:
					print('請輸入正確指令')
		elif pages > page > 1 :
			while True:
				turnpage = input('請輸入a至上一頁或輸入d至下一頁:')
				if turnpage == 'a':
					page -= 1
					break
				elif turnpage == 'd':
					page += 1
					break
				else:
					print('請輸入正確指令')
		elif page == pages:
			while True:
				turnpage = input('請輸入a至上一頁或輸入q回到menu:')
				if turnpage == 'a':
					page -= 1
					break
				elif turnpage == 'q':
					page += 1
					break
				else:
					print('請輸入正確指令')


def timeRange(db):
	begin = input('請輸入起始時間:')
	end = input('請輸入結束時間:')
	sql = '''select Date, time, usec, SourceIP, SourcePort, DestinationIP, DestinationPort, FQDN 
		from test where time between '%s' and '%s' order by Date, time, usec;''' % (begin, end)
	db.execute(sql)
	rows = db.fetchall()
	page = 1
	pages = len(rows) // 50
	pages += 1
	while True:
		if page > pages:
			break
		print('+----------+----------+-------+-----------------+------------+-----------------+-----------------+----------------------------------------------------------+')
		print('| Date     | time     | usec  | SourceIP        | SourcePort | DestinationIP   | DestinationPort | FQDN                                                     |')
		print('+----------+----------+-------+-----------------+------------+-----------------+-----------------+----------------------------------------------------------+')
		for row in rows[(page-1)*50: page*50]:
			print('| '+row[0]+' | '+row[1]+' | %5s '%row[2]+'| %15s '%row[3]+'| %10s '%row[4]+'| %15s '%row[5]+'| %15s '%row[6]+'| %56s |'%row[7])
		print('+----------+----------+-------+-----------------+------------+-----------------+-----------------+----------------------------------------------------------+')
		print('第 %d 頁 / 共 %d 頁' % (page, pages))
		if pages == 1:
			while True:
				turnpage = input('請輸入q回到menu:')
				if turnpage == 'q':
					page += 1
					break
				else:
					print('請輸入正確指令')
		elif page == 1:
			while True:
				turnpage = input('請輸入d至下一頁:')
				if turnpage == 'd':
					page += 1
					break
				else:
					print('請輸入正確指令')
		elif pages > page > 1 :
			while True:
				turnpage = input('請輸入a至上一頁或輸入d至下一頁:')
				if turnpage == 'a':
					page -= 1
					break
				elif turnpage == 'd':
					page += 1
					break
				else:
					print('請輸入正確指令')
		elif page == pages:
			while True:
				turnpage = input('請輸入a至上一頁或輸入q回到menu:')
				if turnpage == 'a':
					page -= 1
					break
				elif turnpage == 'q':
					page += 1
					break
				else:
					print('請輸入正確指令')


def fQDN(db):
	url = input('請輸入FQDN:')
	sql = '''select Date, time, usec, SourceIP, SourcePort, DestinationIP, DestinationPort, FQDN 
		from test where FQDN = '%s' order by Date, time, usec;''' % url
	db.execute(sql)
	rows = db.fetchall()
	page = 1
	pages = len(rows) // 50
	pages += 1
	while True:
		if page > pages:
			break
		print('+----------+----------+-------+-----------------+------------+-----------------+-----------------+----------------------------------------------------------+')
		print('| Date     | time     | usec  | SourceIP        | SourcePort | DestinationIP   | DestinationPort | FQDN                                                     |')
		print('+----------+----------+-------+-----------------+------------+-----------------+-----------------+----------------------------------------------------------+')
		for row in rows[(page-1)*50: page*50]:
			print('| '+row[0]+' | '+row[1]+' | %5s '%row[2]+'| %15s '%row[3]+'| %10s '%row[4]+'| %15s '%row[5]+'| %15s '%row[6]+'| %56s |'%row[7])
		print('+----------+----------+-------+-----------------+------------+-----------------+-----------------+----------------------------------------------------------+')
		print('第 %d 頁 / 共 %d 頁' % (page, pages))
		if pages == 1:
			while True:
				turnpage = input('請輸入q回到menu:')
				if turnpage == 'q':
					page += 1
					break
				else:
					print('請輸入正確指令')
		elif page == 1:
			while True:
				turnpage = input('請輸入d至下一頁:')
				if turnpage == 'd':
					page += 1
					break
				else:
					print('請輸入正確指令')
		elif pages > page > 1 :
			while True:
				turnpage = input('請輸入a至上一頁或輸入d至下一頁:')
				if turnpage == 'a':
					page -= 1
					break
				elif turnpage == 'd':
					page += 1
					break
				else:
					print('請輸入正確指令')
		elif page == pages:
			while True:
				turnpage = input('請輸入a至上一頁或輸入q回到menu:')
				if turnpage == 'a':
					page -= 1
					break
				elif turnpage == 'q':
					page += 1
					break
				else:
					print('請輸入正確指令')