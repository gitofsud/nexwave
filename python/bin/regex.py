import csv
import sqlite3
import urllib.request as u

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

myURL = r'https://www.jafsoft.com/searchengines/log_sample.html'
F = u.urlopen(myURL)

# [.] -> . only
# . -> Any char
# \d -> Any digit
# \D -> non-digit
# * -> 0 or more
# + -> 1 or more
# ? -> 0 or 1
# \w -> Word char
# \W -> Non word
# S -> non-space

done = False
import re
if done:
    for line in F:
        line = line.decode() # Converting bytes to str
        m = re.match('(\d\d\d\.\d{3}[.]\d{1,3}\.[0-9]{3}).*?(\d{1,2}/[a-zA-Z]{3}/\d{4}).*(?:GET|POST)\s+/(?:pics/(\w+\.\w+))?.*(http://\S+)</A>.*', line)
        if m is not None:
            ip = m.group(1)
            dt = m.group(2)
            im = m.group(3)
            if im == None:
                im = "No Image"
            wb = m.group(4)
            query = f"INSERT INTO LOGDATA VALUES ('{ip}','{dt}','{im}','{wb}')"
            cur.execute(query)
    con.commit()

cur.execute("SELECT * FROM LOGDATA")
result = cur.fetchall()
print('Result =', result)

F = open('dbdump.csv', 'w', newline="")
wt = csv.writer(F)
wt.writerow(['IP', 'DATE', 'PICS', 'URL'])
for each_row in result:
    wt.writerow(each_row)
F.close()

F = open('dbdump.csv')
rdr = csv.reader(F)
csv_out = list(rdr)
print('CSV:', csv_out)

import pandas as pd
df1 = pd.DataFrame([[10, 20, 30], [40, 50, 60]], index=['r1', 'r2'], columns=['c1', 'c2', 'c3'])
print(df1)

L1 = list([[10, 20, 30], [40, 50, 60]])
print(L1)

df2 = pd.DataFrame(result)
print(df2)

df2.to_csv('out3.csv', index=None, header=['IP', 'DATE', 'PICS', 'URL'])

# ---------------------------------------------------------------
cur.execute("SELECT * FROM LOGDATA")
df3 = pd.DataFrame(cur)
df3.to_csv('out4.csv', index=None, header=['IP', 'DATE', 'PICS', 'URL'])

df3.to_excel('out5.xlsx')
df3.to_json('out6.json')

df4 = df3.T
df4.to_json('out6.json')
