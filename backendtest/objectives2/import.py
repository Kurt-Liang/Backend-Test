import csv
import pymysql

def get_list():
	mylist = []
	with open('output.csv') as csvfile:
		rows = csv.reader(csvfile)
		for row in rows:
			mylist.append(row)
	return mylist

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


if __name__ == '__main__':
	mylist = get_list()
	with DB(user='root', password='password', db='backendtest') as db:
		db.execute("drop table if exists test")
		sql = """create table test(
		    id int primary key auto_increment,
		    Date char(10),
		    time char(10),
		    usec char(10),
		    SourceIP char(30),
		    SourcePort char(10),
		    DestinationIP char(30),
		    DestinationPort char(10),
		    FQDN char(60)
		    );"""
		db.execute(sql)

		for i in mylist:
			date, time, usec, sourceIP, sourcePort, destinationIP, destinationPort, fqdn = i[1], i[2], i[10], i[3], i[7], i[5], i[9], i[11]
			insert = """insert into test(Date, time, usec, SourceIP, SourcePort, DestinationIP, DestinationPort, FQDN)
				values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');""" % (date, time, usec, sourceIP, sourcePort, destinationIP, destinationPort, fqdn)
			db.execute(insert)
		print('OK')


