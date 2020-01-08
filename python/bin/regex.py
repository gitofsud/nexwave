import sqlite3

con = sqlite3.connect('myDB.sqlite3')

# import pymysql
# con = pymysql.connect(user='', password='', host='', port='', database='')

cur = con.cursor()
query = '''
    CREATE TABLE IF NOT EXISTS LOGDATA (
        IP VARCHAR(100),
        DATE VARCHAR(100),
        PICS VARCHAR(100),
        URL VARCHAR(100)
    )
'''

cur.execute(query)

import urllib.request as u

myURL = r'https://www.jafsoft.com/searchengines/log_sample.html'
F = u.urlopen(myURL)

# [.] -> . only
# . -> Any char
# \d -> Any digit
# \D -> non-digit
# * -> 0 or more
# + -> 1 or more
# ? -> 0 or 1

import re
for line in F:
    line = line.decode() # Converting bytes to str
    m = re.match('(\d\d\d\.\d{3}[.]\d{1,3}\.[0-9]{3}).*', line)   # 123.123.123.123
    if m != None:
        ip = m.group(1)
        print(ip)

