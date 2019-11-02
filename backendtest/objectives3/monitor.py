import configparser
import urllib
import os
import datetime
import re
import pytz

# read config.ini
config = configparser.ConfigParser()
config.read('/backendtest/config.ini')
logger = config.get('system', 'logger')
url = config.get('system', 'URL')

# get time
tz = pytz.timezone('Asia/Taipei')
localtime = str(datetime.datetime.now(tz))

# get PID
pid = os.getpid()

# PHP-MySQL connection
try:
	response = urllib.urlopen(url)
	html = response.read().decode("utf-8")
	mes = re.findall(r'{"\w+":"\w+"}', html)[0]
	if mes[-4:-2] == 'OK':
		conn = 'OK'
	else:
		conn = 'ERROR'
	log = "[%s]%s:PID:%d,response:%s\n" % (localtime, conn, pid, mes)

except:
	cont = "ERROR"
	log = "[%s]%s:PID:%d,ERROR-Can't connect to %s\n" % (localtime, conn, pid, url)

if logger == '1':
	with open('test.log', 'a+') as f:
		f.write(log)

print(log)