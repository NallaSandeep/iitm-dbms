import os
import sys
import psycopg2

f = open('date.txt')
a = f.read()
# print(a)
# os.environ['PGUSER'] = "postgres"
# os.environ['PGPASSWORD'] = "S@ndeep056"
# os.environ['PGHOST'] = "localhost"
# os.environ['PGPORT'] = "5432"
database = sys.argv[1]  # name of the database is obtained from the command line argument
user = os.environ.get('PGUSER')
password = os.environ.get('PGPASSWORD')
host = os.environ.get('PGHOST')
port = os.environ.get('PGPORT')
conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
cur = conn.cursor()
stat = '''
select name from referees 
where referee_id in (
select referee from match_referees 
where match_num in (select match_num from matches where match_date=%s))
'''
cur.execute(stat, (a,))
while True:
    row = cur.fetchone()
    # print(row)
    if row is None:
        break
    vs = row[0].split(' ')
    x = vs[-1]
    for i in range(len(vs) - 1):
        x += ' ' + vs[i][0] + '.'
    print(x)
cur.close()
conn.close()
